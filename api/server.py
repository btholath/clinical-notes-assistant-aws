import os
from pathlib import Path
from fastapi import FastAPI, Depends, Request
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer, HTTPAuthorizationCredentials
from openai import OpenAI

app = FastAPI()

# Add CORS middleware (allows frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clerk authentication setup
clerk_config = ClerkConfig(jwks_url=os.getenv("CLERK_JWKS_URL"))
clerk_guard = ClerkHTTPBearer(clerk_config)


class Visit(BaseModel):
    patient_name: str
    date_of_visit: str
    notes: str


system_prompt = """
You are provided with notes written by a doctor from a patient's visit.
Your job is to summarize the visit for the doctor and provide an email.
Reply with exactly three sections with the headings:
### Summary of visit for the doctor's records
### Next steps for the doctor
### Draft of email to patient in patient-friendly language
"""


def user_prompt_for(visit: Visit) -> str:
    return f"""Create the summary, next steps and draft email for:
Patient Name: {visit.patient_name}
Date of Visit: {visit.date_of_visit}
Notes:
{visit.notes}"""


@app.post("/api/consultation")
def consultation_summary(
        visit: Visit,
        creds: HTTPAuthorizationCredentials = Depends(clerk_guard),
):
    user_id = creds.decoded["sub"]
    client = OpenAI()

    user_prompt = user_prompt_for(visit)
    prompt = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
        stream=True,
    )

    def event_stream():
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                lines = text.split("\n")
                for line in lines[:-1]:
                    yield f"data: {line}\n\n"
                    yield "data:  \n"
                yield f"data: {lines[-1]}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/health")
def health_check():
    """Health check endpoint for AWS App Runner"""
    return {"status": "healthy"}


# Serve static files (our Next.js export) - MUST BE LAST!
static_path = Path("static")
if static_path.exists():
    # Mount static files for assets (_next, images, etc.)
    # This needs to be mounted BEFORE the catch-all route
    app.mount("/_next", StaticFiles(directory="static/_next"), name="next-static")


    # Serve index.html for the root path
    @app.get("/")
    async def serve_root():
        return FileResponse(static_path / "index.html")


    # Catch-all route for HTML pages (like /product -> product.html)
    @app.get("/{path:path}")
    async def serve_pages(path: str):
        # First, check if it's a direct file request (like favicon.ico)
        file_path = static_path / path
        if file_path.is_file():
            return FileResponse(file_path)

        # Check for .html file (e.g., /product -> product.html)
        html_path = static_path / f"{path}.html"
        if html_path.is_file():
            return FileResponse(html_path)

        # Check for index.html in subdirectory (e.g., /about/ -> about/index.html)
        index_path = static_path / path / "index.html"
        if index_path.is_file():
            return FileResponse(index_path)

        # Fallback to 404.html if it exists, otherwise return index for SPA behavior
        not_found_path = static_path / "404.html"
        if not_found_path.is_file():
            return FileResponse(not_found_path, status_code=404)

        # Final fallback - return index.html (useful for client-side routing)
        return FileResponse(static_path / "index.html")