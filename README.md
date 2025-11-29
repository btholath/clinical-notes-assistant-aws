# 🏥 Clinical Notes Assistant

> **AI-Powered Healthcare Consultation Assistant** - Transform doctor's notes into professional summaries, actionable items, and patient-friendly communications.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-AWS%20App%20Runner-orange?style=for-the-badge)](https://2bwrwvweqr.us-east-1.awsapprunner.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat-square&logo=typescript)](https://www.typescriptlang.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-App%20Runner-FF9900?style=flat-square&logo=amazon-aws)](https://aws.amazon.com/apprunner/)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [File Descriptions](#-file-descriptions)
- [Prerequisites](#-prerequisites)
- [Local Development Setup](#-local-development-setup)
- [Docker Configuration](#-docker-configuration)
- [AWS Deployment Guide](#-aws-deployment-guide)
- [Environment Variables](#-environment-variables)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## 🎯 Overview

Clinical Notes Assistant is a production-ready healthcare SaaS application that leverages AI to streamline clinical documentation workflows. Healthcare providers can input consultation notes and receive:

- **Professional Medical Summaries** - Structured summaries suitable for medical records
- **Actionable Next Steps** - Clear follow-up tasks for clinicians
- **Patient-Friendly Emails** - Draft communications in plain language

### Key Features

| Feature | Description |
|---------|-------------|
| 🔐 **Secure Authentication** | User authentication via Clerk with subscription management |
| 💳 **Subscription Plans** | Premium subscription handling with Clerk's PricingTable |
| ⚡ **Real-Time Streaming** | Server-Sent Events (SSE) for live AI response streaming |
| 🐳 **Containerized** | Single Docker container serving both frontend and backend |
| ☁️ **Cloud-Native** | Deployed on AWS App Runner with auto-scaling |

---

## 🌐 Live Demo

**Production URL:** [https://2bwrwvweqr.us-east-1.awsapprunner.com/](https://2bwrwvweqr.us-east-1.awsapprunner.com/)

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        AWS App Runner                           │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    Docker Container                        │  │
│  │                                                            │  │
│  │  ┌─────────────────┐    ┌─────────────────────────────┐   │  │
│  │  │  Static Files   │    │      FastAPI Server         │   │  │
│  │  │  (Next.js SSG)  │    │      (Python 3.12)          │   │  │
│  │  │                 │    │                             │   │  │
│  │  │  • index.html   │    │  • /api/consultation (POST) │   │  │
│  │  │  • product.html │    │  • /health (GET)            │   │  │
│  │  │  • _next/*      │    │  • Static file serving      │   │  │
│  │  └─────────────────┘    └─────────────────────────────┘   │  │
│  │           │                          │                     │  │
│  │           └──────────┬───────────────┘                     │  │
│  │                      │                                     │  │
│  │              Uvicorn (Port 8000)                           │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
    ┌──────────┐       ┌──────────┐        ┌──────────┐
    │  Clerk   │       │  OpenAI  │        │   AWS    │
    │   Auth   │       │   API    │        │   ECR    │
    └──────────┘       └──────────┘        └──────────┘
```

### How It Works

1. **Build Phase**: Next.js compiles to static HTML/JS files (`output: 'export'`)
2. **Container**: Single Docker image contains both static files and Python server
3. **Runtime**: FastAPI serves static files AND handles API requests
4. **Authentication**: Clerk handles user auth on client-side, JWT validation on server
5. **AI Processing**: OpenAI API generates consultation summaries with streaming

---

## 🛠 Tech Stack

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| [Next.js](https://nextjs.org/) | 15.x | React framework with Pages Router |
| [React](https://reactjs.org/) | 19.x | UI library |
| [TypeScript](https://www.typescriptlang.org/) | 5.x | Type safety |
| [Tailwind CSS](https://tailwindcss.com/) | 3.x | Utility-first styling |
| [Clerk](https://clerk.com/) | Latest | Authentication & subscriptions |
| [React DatePicker](https://reactdatepicker.com/) | Latest | Date selection component |
| [React Markdown](https://github.com/remarkjs/react-markdown) | Latest | Markdown rendering |

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| [Python](https://www.python.org/) | 3.12 | Runtime |
| [FastAPI](https://fastapi.tiangolo.com/) | Latest | API framework |
| [Uvicorn](https://www.uvicorn.org/) | Latest | ASGI server |
| [OpenAI SDK](https://github.com/openai/openai-python) | Latest | AI completions |
| [fastapi-clerk-auth](https://pypi.org/project/fastapi-clerk-auth/) | Latest | JWT validation |
| [Pydantic](https://pydantic.dev/) | Latest | Data validation |

### Infrastructure
| Technology | Purpose |
|------------|---------|
| [Docker](https://www.docker.com/) | Containerization |
| [AWS ECR](https://aws.amazon.com/ecr/) | Container registry |
| [AWS App Runner](https://aws.amazon.com/apprunner/) | Serverless container hosting |

---

## 📁 Project Structure

```
clinical-notes-assistant-aws/
├── pages/                    # Next.js Pages Router
│   ├── _app.tsx             # App wrapper with ClerkProvider
│   ├── _document.tsx        # Custom HTML document
│   ├── index.tsx            # Landing page (public)
│   └── product.tsx          # Main app (protected)
│
├── api/                      # Backend
│   └── server.py            # FastAPI application
│
├── styles/                   # Styling
│   └── globals.css          # Global styles + Tailwind imports
│
├── public/                   # Static assets
│
├── Dockerfile               # Multi-stage Docker build
├── next.config.ts           # Next.js configuration
├── tsconfig.json            # TypeScript configuration
├── package.json             # Node.js dependencies
├── requirements.txt         # Python dependencies
├── .env.local               # Local environment variables (git-ignored)
└── .dockerignore            # Docker build exclusions
```

---

## 📄 File Descriptions

### Frontend Files

#### `pages/_app.tsx`
The root application component that wraps all pages with the ClerkProvider for authentication context.

```tsx
// Wraps the entire application with Clerk authentication
// Imports global CSS and date picker styles
// Provides authentication context to all child components
```

**Key responsibilities:**
- Initialize Clerk authentication
- Import global stylesheets
- Provide authentication context to all pages

---

#### `pages/_document.tsx`
Custom HTML document that defines the base HTML structure.

```tsx
// Sets document language to English
// Defines meta tags for SEO
// Sets up the document title
```

**Key responsibilities:**
- Define `<html>` and `<body>` structure
- Add meta tags and title
- Set document language

---

#### `pages/index.tsx`
The public landing page showcasing the application features.

```tsx
// Public landing page with:
// - Navigation with sign-in button
// - Hero section with product description
// - Feature cards (Professional Summaries, Action Items, Patient Emails)
// - Call-to-action buttons
// - Uses SignedIn/SignedOut components for conditional rendering
```

**Key responsibilities:**
- Marketing/landing content
- Sign-in/Sign-up buttons via Clerk
- Redirect to `/product` when authenticated

---

#### `pages/product.tsx`
The main application page (protected, requires authentication and subscription).

```tsx
// Protected consultation form page with:
// - ConsultationForm component for input
// - Clerk's <Protect> component for subscription gating
// - PricingTable fallback for non-subscribers
// - Real-time streaming AI responses
// - Markdown rendering of results
```

**Key features:**
- **Authentication Guard**: Uses `<Protect plan="premium_subscription">` to gate access
- **Form Inputs**: Patient name, date of visit, consultation notes
- **Streaming**: Uses `fetchEventSource` for Server-Sent Events
- **Output Display**: ReactMarkdown with GFM support

---

#### `next.config.ts`
Next.js configuration for static export.

```typescript
const nextConfig: NextConfig = {
  output: 'export',        // Generate static HTML files
  images: {
    unoptimized: true      // Required for static export
  }
};
```

**Key configuration:**
- `output: 'export'` - Enables Static Site Generation (SSG)
- Generates files in `/out` directory during build
- No server-side rendering (all client-side)

---

#### `tsconfig.json`
TypeScript configuration optimized for Next.js.

```json
{
  "compilerOptions": {
    "target": "ES2017",
    "jsx": "react-jsx",
    "moduleResolution": "bundler",
    "strict": true
  }
}
```

**Key settings:**
- Strict mode enabled for type safety
- React JSX transform (no React import needed)
- Path aliases with `@/*` mapping

---

### Backend Files

#### `api/server.py`
The FastAPI backend server that handles API requests and serves static files.

```python
# FastAPI application with:
# - CORS middleware for cross-origin requests
# - Clerk JWT authentication
# - OpenAI streaming integration
# - Static file serving for Next.js export
# - Health check endpoint for App Runner
```

**Endpoints:**

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/consultation` | Generate AI consultation summary |
| `GET` | `/health` | Health check for App Runner |
| `GET` | `/` | Serve index.html |
| `GET` | `/{path}` | Serve static files |

**Key components:**

1. **CORS Middleware**: Allows frontend to call backend
2. **Clerk Authentication**: Validates JWT tokens via JWKS
3. **Visit Model**: Pydantic model for request validation
4. **Streaming Response**: Server-Sent Events for real-time output
5. **Static File Serving**: Serves Next.js exported files

---

### Docker Configuration

#### `Dockerfile`
Multi-stage Docker build for optimized container size.

```dockerfile
# Stage 1: Build Next.js static files
FROM node:22-alpine AS frontend-builder
# - Installs npm dependencies
# - Builds Next.js app with static export
# - Creates /app/out directory with HTML/JS files

# Stage 2: Create Python runtime container
FROM python:3.12-slim
# - Installs Python dependencies
# - Copies server.py
# - Copies static files from Stage 1
# - Runs Uvicorn server on port 8000
```

**Build stages:**

| Stage | Base Image | Purpose | Output |
|-------|------------|---------|--------|
| 1 | `node:22-alpine` | Build Next.js | `/app/out/*` |
| 2 | `python:3.12-slim` | Run FastAPI | Container |

---

## ✅ Prerequisites

Before you begin, ensure you have the following:

### Software Requirements

| Software | Minimum Version | Installation |
|----------|-----------------|--------------|
| Node.js | 20.x | [nodejs.org](https://nodejs.org/) |
| Python | 3.10+ | [python.org](https://www.python.org/) |
| Docker | 20.x | [docker.com](https://www.docker.com/) |
| AWS CLI | 2.x | [AWS CLI Install](https://aws.amazon.com/cli/) |
| Git | Latest | [git-scm.com](https://git-scm.com/) |

### Service Accounts

| Service | Purpose | Sign Up |
|---------|---------|---------|
| Clerk | Authentication & subscriptions | [clerk.com](https://clerk.com/) |
| OpenAI | AI text generation | [platform.openai.com](https://platform.openai.com/) |
| AWS | Cloud hosting | [aws.amazon.com](https://aws.amazon.com/) |

---

## 🚀 Local Development Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/btholath/clinical-notes-assistant-aws.git
cd clinical-notes-assistant-aws
```

### Step 2: Install Frontend Dependencies

```bash
npm install
```

### Step 3: Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env.local` file in the project root:

```bash
# Clerk Authentication
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxx
CLERK_SECRET_KEY=sk_test_xxxxxxxxxx
CLERK_JWKS_URL=https://your-clerk-instance.clerk.accounts.dev/.well-known/jwks.json

# OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx

# AWS (for deployment)
DEFAULT_AWS_REGION=us-east-1
AWS_ACCOUNT_ID=123456789012
```

### Step 5: Run Development Servers

**Frontend (Terminal 1):**
```bash
npm run dev
```
Opens at [http://localhost:3000](http://localhost:3000)

**Backend (Terminal 2):**
```bash
cd api
uvicorn server:app --reload --port 8000
```
API at [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Configuration

### Building the Docker Image

#### Step 1: Load Environment Variables

**Mac/Linux:**
```bash
export $(cat .env.local | grep -v '^#' | xargs)
```

**Windows PowerShell:**
```powershell
Get-Content .env.local | ForEach-Object {
    if ($_ -match '^(.+?)=(.+)$') {
        [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
    }
}
```

#### Step 2: Build the Image

**Mac/Linux:**
```bash
docker build \
  --build-arg NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="$NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY" \
  -t consultation-app .
```

**Windows PowerShell:**
```powershell
docker build `
  --build-arg NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="$env:NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY" `
  -t consultation-app .
```

#### Step 3: Run Locally

```bash
docker run -p 8000:8000 \
  -e CLERK_SECRET_KEY="$CLERK_SECRET_KEY" \
  -e CLERK_JWKS_URL="$CLERK_JWKS_URL" \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  consultation-app
```

Open [http://localhost:8000](http://localhost:8000) to test.

### Docker Build Process Explained

```
┌────────────────────────────────────────────────────────────┐
│                    STAGE 1: Frontend Build                  │
├────────────────────────────────────────────────────────────┤
│  1. FROM node:22-alpine                                    │
│  2. COPY package*.json → npm ci                            │
│  3. COPY all source files                                  │
│  4. ARG NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY                  │
│  5. RUN npm run build                                      │
│  6. OUTPUT: /app/out/* (static HTML/JS/CSS)                │
└────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│                    STAGE 2: Python Runtime                  │
├────────────────────────────────────────────────────────────┤
│  1. FROM python:3.12-slim                                  │
│  2. COPY requirements.txt → pip install                    │
│  3. COPY api/server.py                                     │
│  4. COPY --from=Stage1 /app/out → ./static                 │
│  5. EXPOSE 8000                                            │
│  6. CMD uvicorn server:app --host 0.0.0.0 --port 8000      │
└────────────────────────────────────────────────────────────┘
```

---

## ☁️ AWS Deployment Guide

### Overview

The deployment pipeline:

```
Local Build → Push to ECR → Deploy to App Runner
```

### Step 1: AWS Account Setup

#### 1.1 Create IAM User for Deployment

1. Go to **IAM Console** → **Users** → **Create User**
2. Name: `clinical-notes-deployer`
3. Attach policies:
   - `AmazonEC2ContainerRegistryFullAccess`
   - `AWSAppRunnerFullAccess`

4. Create access keys and save them securely

#### 1.2 Configure AWS CLI

```bash
aws configure
# Enter your Access Key ID
# Enter your Secret Access Key
# Region: us-east-1 (or your preferred region)
# Output format: json
```

### Step 2: Create ECR Repository

```bash
# Set variables
AWS_REGION=us-east-1
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPO=clinical-notes-assistant

# Create ECR repository
aws ecr create-repository \
  --repository-name $ECR_REPO \
  --region $AWS_REGION
```

### Step 3: Build and Push to ECR

#### 3.1 Authenticate Docker with ECR

```bash
aws ecr get-login-password --region $AWS_REGION | \
  docker login --username AWS --password-stdin \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

#### 3.2 Build the Image

```bash
docker build \
  --build-arg NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="$NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY" \
  -t consultation-app .
```

#### 3.3 Tag for ECR

```bash
docker tag consultation-app:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest
```

#### 3.4 Push to ECR

```bash
docker push \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest
```

### Step 4: Deploy to AWS App Runner

#### 4.1 Create App Runner Service (Console)

1. Go to **AWS App Runner Console**
2. Click **Create service**
3. **Source configuration:**
   - Repository type: **Container registry**
   - Provider: **Amazon ECR**
   - Select your repository and `latest` tag
   
4. **Deployment settings:**
   - Deployment trigger: **Manual** (or Automatic)
   - ECR access role: Create new or use existing

5. **Service settings:**
   - Service name: `clinical-notes-assistant`
   - Port: `8000`
   - CPU: 1 vCPU
   - Memory: 2 GB

6. **Environment variables:**
   
   | Key | Value |
   |-----|-------|
   | `CLERK_SECRET_KEY` | `sk_live_xxx` |
   | `CLERK_JWKS_URL` | `https://xxx.clerk.accounts.dev/.well-known/jwks.json` |
   | `OPENAI_API_KEY` | `sk-xxx` |

7. **Health check:**
   - Path: `/health`
   - Protocol: HTTP

8. Click **Create & deploy**

#### 4.2 Create App Runner Service (CLI)

```bash
# Create service configuration file
cat > apprunner-config.json << EOF
{
  "ServiceName": "clinical-notes-assistant",
  "SourceConfiguration": {
    "ImageRepository": {
      "ImageIdentifier": "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest",
      "ImageRepositoryType": "ECR",
      "ImageConfiguration": {
        "Port": "8000",
        "RuntimeEnvironmentVariables": {
          "CLERK_SECRET_KEY": "$CLERK_SECRET_KEY",
          "CLERK_JWKS_URL": "$CLERK_JWKS_URL",
          "OPENAI_API_KEY": "$OPENAI_API_KEY"
        }
      }
    },
    "AuthenticationConfiguration": {
      "AccessRoleArn": "arn:aws:iam::$AWS_ACCOUNT_ID:role/AppRunnerECRAccessRole"
    }
  },
  "InstanceConfiguration": {
    "Cpu": "1024",
    "Memory": "2048"
  },
  "HealthCheckConfiguration": {
    "Protocol": "HTTP",
    "Path": "/health",
    "Interval": 10,
    "Timeout": 5,
    "HealthyThreshold": 1,
    "UnhealthyThreshold": 5
  }
}
EOF

# Create the service
aws apprunner create-service --cli-input-json file://apprunner-config.json
```

### Step 5: Configure Clerk for Production

1. Go to **Clerk Dashboard** → Your Application
2. Navigate to **Domains**
3. Add your App Runner URL: `https://xxxxx.us-east-1.awsapprunner.com`
4. Save changes

### Step 6: Verify Deployment

1. Get your App Runner URL from the console
2. Visit the URL in your browser
3. Test sign-in and consultation features
4. Check `/health` endpoint returns `{"status": "healthy"}`

---

## 🔐 Environment Variables

### Required Variables

| Variable | Description | Where Used |
|----------|-------------|------------|
| `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` | Clerk public key (pk_*) | Frontend (build-time) |
| `CLERK_SECRET_KEY` | Clerk secret key (sk_*) | Backend (runtime) |
| `CLERK_JWKS_URL` | Clerk JWKS endpoint | Backend (runtime) |
| `OPENAI_API_KEY` | OpenAI API key | Backend (runtime) |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEFAULT_AWS_REGION` | AWS region | `us-east-1` |
| `AWS_ACCOUNT_ID` | AWS account ID | - |

### Getting Your Keys

#### Clerk Keys
1. Go to [Clerk Dashboard](https://dashboard.clerk.com/)
2. Select your application
3. Go to **API Keys**
4. Copy **Publishable Key** and **Secret Key**
5. JWKS URL format: `https://<your-clerk-instance>.clerk.accounts.dev/.well-known/jwks.json`

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create new API key
3. Copy and save securely

---

## 🔧 Troubleshooting

### Common Issues

#### 1. 404 Error on `/product` Page

**Problem:** Static export creates `product.html` but link points to `/product`

**Solution:** Update `server.py` to handle clean URLs:

```python
@app.get("/{path:path}")
async def serve_pages(path: str):
    # Check for .html file
    html_path = static_path / f"{path}.html"
    if html_path.is_file():
        return FileResponse(html_path)
```

#### 2. "Illegal header value" Error with OpenAI

**Problem:** Environment variable has carriage return (`\r`)

**Cause:** `.env` file edited on Windows

**Solution:**
```bash
# Fix line endings
sed -i 's/\r$//' .env.local

# Or reload with cleaned values
docker run -p 8000:8000 \
  -e OPENAI_API_KEY="$(echo $OPENAI_API_KEY | tr -d '\r')" \
  consultation-app
```

#### 3. Clerk Authentication Fails in Production

**Problem:** User can't sign in on deployed app

**Solutions:**
1. Add App Runner URL to Clerk allowed domains
2. Verify `CLERK_JWKS_URL` is correct
3. Check `CLERK_SECRET_KEY` matches production environment

#### 4. Docker Build Fails

**Problem:** `npm ci` or `pip install` fails

**Solutions:**
```bash
# Clear Docker cache
docker builder prune -a

# Rebuild without cache
docker build --no-cache \
  --build-arg NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="$NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY" \
  -t consultation-app .
```

#### 5. App Runner Health Check Fails

**Problem:** Service won't start, health check timeout

**Solutions:**
1. Verify `/health` endpoint returns 200
2. Increase health check timeout (5s → 10s)
3. Check App Runner logs in CloudWatch

---

## 📊 Cost Estimation

### AWS App Runner (approximate monthly costs)

| Resource | Configuration | Est. Cost |
|----------|--------------|-----------|
| Compute | 1 vCPU, 2GB RAM | ~$25-50/mo |
| Requests | Per million | ~$1/million |
| ECR Storage | Per GB | ~$0.10/GB |

### Other Services

| Service | Tier | Cost |
|---------|------|------|
| Clerk | Free tier | $0 (up to 10k MAU) |
| OpenAI | Pay per use | Variable |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Biju Tholath**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/biju-tholath/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/btholath)

---

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) - React Framework
- [FastAPI](https://fastapi.tiangolo.com/) - Python API Framework
- [Clerk](https://clerk.com/) - Authentication Platform
- [OpenAI](https://openai.com/) - AI Platform
- [AWS](https://aws.amazon.com/) - Cloud Infrastructure

---

<p align="center">
  Built with ❤️ for Healthcare Providers
</p>
