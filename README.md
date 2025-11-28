<p align="center">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Clerk-6C47FF?style=for-the-badge&logo=clerk&logoColor=white" alt="Clerk" />
</p>

<h1 align="center">🏥 Clinical Notes Assistant</h1>

<p align="center">
  <strong>AI-Powered Healthcare Consultation Assistant</strong><br>
  Transform doctor's notes into professional summaries, actionable items, and patient-friendly communications
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-prerequisites">Prerequisites</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-testing">Testing</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
  <img src="https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen" alt="Node Version" />
  <img src="https://img.shields.io/badge/python-%3E%3D3.10-blue" alt="Python Version" />
</p>

---

## 📋 Overview

**Clinical Notes Assistant** is a production-ready healthcare application designed to streamline clinical documentation workflows. It leverages AI to transform raw consultation notes into structured, professional outputs—reducing administrative burden for healthcare providers and improving patient communication.

### The Problem

Healthcare providers spend an average of **2 hours per day** on documentation tasks. This administrative burden leads to:
- Physician burnout
- Reduced patient interaction time
- Inconsistent documentation quality
- Delayed patient communications

### The Solution

Clinical Notes Assistant automates the transformation of consultation notes into:
- **Professional medical summaries** for records
- **Actionable next steps** for follow-up care
- **Patient-friendly emails** for clear communication

All generated in **real-time** with AI streaming, so providers see results instantly.

---

## ✨ Features

### Core Functionality

| Feature | Description |
|---------|-------------|
| 📝 **Smart Note Input** | Structured forms with date pickers for consultation details |
| 📋 **Medical Summaries** | AI-generated professional summaries for medical records |
| ✅ **Action Items** | Extracted and organized follow-up tasks for clinicians |
| 📧 **Patient Emails** | Auto-drafted patient-friendly email communications |
| ⚡ **Real-Time Streaming** | Watch AI-generated content appear instantly |
| 🔐 **Secure Authentication** | HIPAA-conscious authentication via Clerk |

### Technical Features

| Feature | Description |
|---------|-------------|
| 🎨 **Modern UI** | Clean, responsive interface built with React & Tailwind CSS |
| 📱 **Responsive Design** | Works seamlessly on desktop, tablet, and mobile |
| 🔄 **Hot Reload** | Fast development with automatic page updates |
| 📊 **Type Safety** | Full TypeScript + Python type coverage |
| 🧪 **Testable** | Comprehensive test coverage with Jest and Pytest |

---

## 🎯 Demo

### Input: Doctor's Consultation Notes
```
Patient: John Smith, 45M
Chief Complaint: Persistent lower back pain x 2 weeks
History: Pain radiates to left leg, worse with sitting
Exam: Limited lumbar flexion, positive straight leg raise left
Assessment: Lumbar radiculopathy, likely L4-L5
Plan: MRI lumbar spine, PT referral, NSAIDs, follow-up 2 weeks
```

### Output 1: Professional Medical Summary
```
CONSULTATION SUMMARY
Patient: John Smith | DOB: [Date] | MRN: [Number]
Date of Service: November 28, 2025

CLINICAL PRESENTATION:
45-year-old male presenting with two-week history of persistent 
lower back pain with radicular symptoms to the left lower extremity...

ASSESSMENT:
Lumbar radiculopathy, clinically consistent with L4-L5 involvement...

PLAN:
1. Diagnostic imaging: MRI lumbar spine without contrast
2. Referral: Physical therapy for core strengthening and McKenzie protocol
3. Pharmacotherapy: NSAID therapy as prescribed
4. Follow-up: Return visit in 2 weeks for imaging review
```

### Output 2: Action Items
```
☐ Order MRI lumbar spine (without contrast)
☐ Submit PT referral - include radiculopathy diagnosis
☐ Prescribe: Naproxen 500mg BID x 14 days
☐ Schedule 2-week follow-up appointment
☐ Send patient education materials on lumbar radiculopathy
```

### Output 3: Patient-Friendly Email
```
Subject: Your Visit Summary & Next Steps - Dr. [Name]'s Office

Dear John,

Thank you for visiting us today. I wanted to follow up with a summary 
of our discussion and your next steps...

[Clear, jargon-free explanation of condition and treatment plan]

Please don't hesitate to contact us if you have any questions.

Best regards,
[Provider Name]
```

---

## 🛠 Tech Stack

### Frontend

| Technology | Version | Purpose |
|------------|---------|---------|
| [Next.js](https://nextjs.org/) | 14.x | React framework with SSR/SSG |
| [React](https://reactjs.org/) | 18.x | UI component library |
| [TypeScript](https://www.typescriptlang.org/) | 5.x | Type-safe JavaScript |
| [Tailwind CSS](https://tailwindcss.com/) | 3.x | Utility-first CSS framework |
| [React DatePicker](https://reactdatepicker.com/) | 4.x | Date selection component |
| [React Hook Form](https://react-hook-form.com/) | 7.x | Form state management |

### Backend

| Technology | Version | Purpose |
|------------|---------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | 0.100+ | High-performance Python API |
| [Python](https://www.python.org/) | 3.10+ | Backend programming language |
| [Pydantic](https://pydantic-docs.helpmanual.io/) | 2.x | Data validation & serialization |
| [OpenAI API](https://openai.com/api/) | Latest | AI text generation |
| [SSE-Starlette](https://github.com/sysid/sse-starlette) | 1.x | Server-Sent Events for streaming |

### Infrastructure & Services

| Technology | Purpose |
|------------|---------|
| [Clerk](https://clerk.com/) | Authentication & user management |
| [Vercel](https://vercel.com/) | Frontend deployment & hosting |
| [Railway](https://railway.app/) / AWS | Backend deployment |
| [PostgreSQL](https://www.postgresql.org/) | Database (optional) |
| [Docker](https://www.docker.com/) | Containerization |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software

| Software | Minimum Version | Check Command |
|----------|-----------------|---------------|
| Node.js | 20.0.0 | `node --version` |
| npm/yarn/pnpm | Latest | `npm --version` |
| Python | 3.10 | `python --version` |
| pip | Latest | `pip --version` |
| Git | Latest | `git --version` |

### Required Accounts & API Keys

| Service | Purpose | Sign Up |
|---------|---------|---------|
| OpenAI | AI text generation | [platform.openai.com](https://platform.openai.com/) |
| Clerk | Authentication | [clerk.com](https://clerk.com/) |
| Stripe (Optional) | Payments | [stripe.com](https://stripe.com/) |

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/btholath/clinical-notes-assistant.git
cd clinical-notes-assistant
```

### Step 2: Frontend Setup

#### 2.1 Install Node.js Dependencies

```bash
# Using npm
npm install

# Or using yarn
yarn install

# Or using pnpm
pnpm install
```

#### 2.2 Create Environment File

```bash
cp .env.example .env.local
```

#### 2.3 Configure Frontend Environment Variables

Edit `.env.local` with your credentials:

```env
# ===========================================
# CLERK AUTHENTICATION
# ===========================================
# Get these from: https://dashboard.clerk.com
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxx
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxx

# Clerk URLs
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/dashboard

# ===========================================
# API CONFIGURATION
# ===========================================
NEXT_PUBLIC_API_URL=http://localhost:8000

# ===========================================
# STRIPE (Optional - for subscriptions)
# ===========================================
# Get these from: https://dashboard.stripe.com/apikeys
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxxxxxxx
```

#### 2.4 Start Frontend Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

### Step 3: Backend Setup

#### 3.1 Navigate to Backend Directory

```bash
cd backend
```

#### 3.2 Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows (Command Prompt):
venv\Scripts\activate.bat

# On Windows (PowerShell):
venv\Scripts\Activate.ps1
```

#### 3.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 3.4 Create Backend Environment File

```bash
cp .env.example .env
```

#### 3.5 Configure Backend Environment Variables

Edit `.env` with your credentials:

```env
# ===========================================
# APPLICATION SETTINGS
# ===========================================
APP_ENV=development
DEBUG=True
SECRET_KEY=your-super-secret-key-change-in-production

# ===========================================
# AI PROVIDER - OpenAI
# ===========================================
# Get from: https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Model Configuration
OPENAI_MODEL=gpt-4
# Options: gpt-4, gpt-4-turbo, gpt-3.5-turbo

# ===========================================
# AI PROVIDER - Anthropic (Alternative)
# ===========================================
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxx

# ===========================================
# DATABASE (Optional)
# ===========================================
DATABASE_URL=postgresql://user:password@localhost:5432/clinical_notes_db

# ===========================================
# CLERK AUTHENTICATION
# ===========================================
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxx

# ===========================================
# CORS SETTINGS
# ===========================================
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# ===========================================
# STRIPE (Optional)
# ===========================================
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxxxxxxx
```

#### 3.6 Start Backend Development Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000).

#### 3.7 Verify Installation

- **API Health Check:** [http://localhost:8000/health](http://localhost:8000/health)
- **Swagger Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📁 Project Structure

```
clinical-notes-assistant/
│
├── 📂 pages/                          # Next.js pages (file-based routing)
│   ├── 📂 api/                        # Next.js API routes
│   │   ├── generate-summary.ts        # AI summary generation endpoint
│   │   ├── generate-actions.ts        # Action items generation endpoint
│   │   └── generate-email.ts          # Patient email generation endpoint
│   │
│   ├── _app.tsx                       # App wrapper with providers
│   ├── _document.tsx                  # Custom HTML document
│   ├── index.tsx                      # Landing page
│   ├── dashboard.tsx                  # Main consultation interface
│   ├── sign-in/[[...index]].tsx       # Clerk sign-in page
│   └── sign-up/[[...index]].tsx       # Clerk sign-up page
│
├── 📂 components/                     # React components
│   ├── 📂 ui/                         # Reusable UI primitives
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   ├── DatePicker.tsx
│   │   └── LoadingSpinner.tsx
│   │
│   ├── 📂 forms/                      # Form components
│   │   ├── ConsultationForm.tsx       # Main consultation input form
│   │   └── PatientInfoForm.tsx        # Patient details form
│   │
│   ├── 📂 outputs/                    # AI output display components
│   │   ├── MedicalSummary.tsx         # Summary display with streaming
│   │   ├── ActionItems.tsx            # Action items checklist
│   │   └── PatientEmail.tsx           # Email preview component
│   │
│   ├── Header.tsx                     # Navigation header
│   ├── Footer.tsx                     # Footer component
│   └── StreamingText.tsx              # Real-time text streaming component
│
├── 📂 lib/                            # Utilities and configurations
│   ├── api.ts                         # API client functions
│   ├── openai.ts                      # OpenAI client configuration
│   ├── prompts.ts                     # AI prompt templates
│   └── utils.ts                       # Helper functions
│
├── 📂 hooks/                          # Custom React hooks
│   ├── useConsultation.ts             # Consultation state management
│   ├── useStreaming.ts                # SSE streaming hook
│   └── useAuth.ts                     # Authentication hook
│
├── 📂 types/                          # TypeScript type definitions
│   ├── consultation.ts                # Consultation-related types
│   ├── api.ts                         # API request/response types
│   └── index.ts                       # Type exports
│
├── 📂 styles/                         # Styling
│   └── globals.css                    # Global CSS with Tailwind imports
│
├── 📂 public/                         # Static assets
│   ├── favicon.ico
│   └── images/
│       └── logo.svg
│
├── 📂 backend/                        # FastAPI backend
│   ├── 📂 app/
│   │   ├── 📂 api/                    # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── routes.py              # Main API routes
│   │   │   ├── consultation.py        # Consultation endpoints
│   │   │   └── health.py              # Health check endpoint
│   │   │
│   │   ├── 📂 services/               # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py          # OpenAI integration
│   │   │   ├── summary_service.py     # Summary generation logic
│   │   │   ├── action_service.py      # Action items logic
│   │   │   └── email_service.py       # Email generation logic
│   │   │
│   │   ├── 📂 models/                 # Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── consultation.py        # Consultation data models
│   │   │   └── responses.py           # API response models
│   │   │
│   │   ├── 📂 core/                   # Core configurations
│   │   │   ├── __init__.py
│   │   │   ├── config.py              # App configuration
│   │   │   └── prompts.py             # AI prompt templates
│   │   │
│   │   └── __init__.py
│   │
│   ├── 📂 tests/                      # Backend tests
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   ├── test_services.py
│   │   └── conftest.py                # Pytest fixtures
│   │
│   ├── main.py                        # FastAPI application entry
│   ├── requirements.txt               # Python dependencies
│   ├── Dockerfile                     # Docker configuration
│   └── .env.example                   # Environment template
│
├── 📂 tests/                          # Frontend tests
│   ├── components/
│   └── pages/
│
├── .env.local                         # Frontend environment (git-ignored)
├── .env.example                       # Frontend environment template
├── .gitignore                         # Git ignore rules
├── .eslintrc.json                     # ESLint configuration
├── .prettierrc                        # Prettier configuration
├── next.config.js                     # Next.js configuration
├── tailwind.config.js                 # Tailwind CSS configuration
├── tsconfig.json                      # TypeScript configuration
├── package.json                       # Node.js dependencies
├── docker-compose.yml                 # Docker Compose configuration
├── LICENSE                            # MIT License
└── README.md                          # This file
```

---

## ⚙️ Configuration

### Clerk Authentication Setup

1. **Create a Clerk Application**
   - Go to [clerk.com](https://clerk.com) and sign up
   - Click **Add Application**
   - Choose your sign-in options (Email, Google, etc.)

2. **Get Your API Keys**
   - Navigate to **API Keys** in the Clerk dashboard
   - Copy `Publishable Key` → `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
   - Copy `Secret Key` → `CLERK_SECRET_KEY`

3. **Configure Redirect URLs**
   - Go to **Paths** in settings
   - Set:
     | Setting | Value |
     |---------|-------|
     | Sign-in URL | `/sign-in` |
     | Sign-up URL | `/sign-up` |
     | After sign-in URL | `/dashboard` |
     | After sign-up URL | `/dashboard` |

4. **Add Allowed Origins** (for production)
   - Go to **Domains** → Add your production domain

---

### OpenAI Configuration

1. **Get Your API Key**
   - Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy to `OPENAI_API_KEY` in backend `.env`

2. **Choose Your Model**
   
   | Model | Best For | Cost |
   |-------|----------|------|
   | `gpt-4` | Highest quality medical summaries | $$$ |
   | `gpt-4-turbo` | Balance of quality and speed | $$ |
   | `gpt-3.5-turbo` | Faster, more economical | $ |

3. **Set Usage Limits** (Recommended)
   - Go to OpenAI dashboard → **Usage Limits**
   - Set monthly spending cap to avoid surprise bills

---

### AI Prompt Customization

The AI prompts are defined in `backend/app/core/prompts.py`. You can customize them for your specific use case:

```python
# backend/app/core/prompts.py

MEDICAL_SUMMARY_PROMPT = """
You are a medical documentation assistant. Given the following 
consultation notes, generate a professional medical summary suitable 
for inclusion in the patient's medical record.

Guidelines:
- Use standard medical terminology
- Be concise but comprehensive
- Include all relevant clinical findings
- Structure with clear headings

Consultation Notes:
{notes}

Generate the medical summary:
"""

ACTION_ITEMS_PROMPT = """
Extract actionable items from the following consultation notes.
Format as a checklist that the healthcare provider can use for follow-up.

Consultation Notes:
{notes}

Generate action items:
"""

PATIENT_EMAIL_PROMPT = """
Draft a patient-friendly email summarizing the consultation.
- Use simple, non-medical language
- Be warm and reassuring
- Include clear next steps
- Avoid medical jargon

Consultation Notes:
{notes}

Patient Name: {patient_name}

Generate the patient email:
"""
```

---

## 📖 Usage

### Basic Workflow

1. **Sign In**
   - Navigate to `/sign-in`
   - Authenticate with Clerk

2. **Enter Consultation Details**
   - Fill in patient information
   - Select consultation date using the date picker
   - Enter your clinical notes in the text area

3. **Generate Outputs**
   - Click **Generate Summary** → View professional medical summary
   - Click **Generate Actions** → View follow-up action items
   - Click **Generate Email** → View patient-friendly email draft

4. **Review & Use**
   - Copy generated content to your EMR/EHR
   - Check off action items as completed
   - Send or customize the patient email

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + Enter` | Generate all outputs |
| `Ctrl/Cmd + S` | Generate summary only |
| `Ctrl/Cmd + A` | Generate actions only |
| `Ctrl/Cmd + E` | Generate email only |
| `Esc` | Clear current output |

---

## 📡 API Reference

### Base URL

- **Development:** `http://localhost:8000`
- **Production:** `https://api.yourdomain.com`

### Authentication

All API endpoints require authentication via Clerk JWT token:

```bash
Authorization: Bearer <clerk_jwt_token>
```

### Endpoints

#### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-11-28T10:30:00Z"
}
```

---

#### Generate Medical Summary

```http
POST /api/v1/consultation/summary
Content-Type: application/json
```

**Request Body:**
```json
{
  "patient_name": "John Smith",
  "patient_dob": "1980-05-15",
  "consultation_date": "2025-11-28",
  "notes": "Patient presents with persistent lower back pain...",
  "stream": true
}
```

**Response (Streaming):**
```
data: {"content": "CONSULTATION", "done": false}
data: {"content": " SUMMARY\n\n", "done": false}
data: {"content": "Patient: John Smith...", "done": false}
...
data: {"content": "", "done": true}
```

**Response (Non-Streaming):**
```json
{
  "summary": "CONSULTATION SUMMARY\n\nPatient: John Smith...",
  "tokens_used": 450,
  "model": "gpt-4"
}
```

---

#### Generate Action Items

```http
POST /api/v1/consultation/actions
Content-Type: application/json
```

**Request Body:**
```json
{
  "notes": "Patient presents with persistent lower back pain...",
  "stream": true
}
```

**Response:**
```json
{
  "actions": [
    { "id": 1, "task": "Order MRI lumbar spine", "priority": "high", "completed": false },
    { "id": 2, "task": "Submit PT referral", "priority": "medium", "completed": false },
    { "id": 3, "task": "Schedule 2-week follow-up", "priority": "medium", "completed": false }
  ]
}
```

---

#### Generate Patient Email

```http
POST /api/v1/consultation/email
Content-Type: application/json
```

**Request Body:**
```json
{
  "patient_name": "John Smith",
  "patient_email": "john.smith@email.com",
  "consultation_date": "2025-11-28",
  "notes": "Patient presents with persistent lower back pain...",
  "provider_name": "Dr. Jane Doe",
  "stream": true
}
```

**Response:**
```json
{
  "subject": "Your Visit Summary & Next Steps - Dr. Doe's Office",
  "body": "Dear John,\n\nThank you for visiting us today...",
  "preview": "Thank you for visiting us today. I wanted to follow up..."
}
```

---

### Error Responses

All errors follow this format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid consultation date format",
    "details": {
      "field": "consultation_date",
      "expected": "YYYY-MM-DD"
    }
  }
}
```

| HTTP Code | Error Code | Description |
|-----------|------------|-------------|
| 400 | `VALIDATION_ERROR` | Invalid request data |
| 401 | `UNAUTHORIZED` | Missing or invalid auth token |
| 403 | `FORBIDDEN` | Insufficient permissions |
| 429 | `RATE_LIMITED` | Too many requests |
| 500 | `INTERNAL_ERROR` | Server error |
| 503 | `AI_SERVICE_ERROR` | OpenAI API unavailable |

---

## 🧪 Testing

### Frontend Testing

#### Run All Tests
```bash
npm run test
```

#### Run Tests in Watch Mode
```bash
npm run test:watch
```

#### Run Tests with Coverage
```bash
npm run test:coverage
```

#### Run Specific Test File
```bash
npm run test -- --testPathPattern="ConsultationForm"
```

### Backend Testing

#### Activate Virtual Environment
```bash
cd backend
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

#### Run All Tests
```bash
pytest
```

#### Run Tests with Verbose Output
```bash
pytest -v
```

#### Run Tests with Coverage
```bash
pytest --cov=app --cov-report=html
# Open htmlcov/index.html in browser to view report
```

#### Run Specific Test File
```bash
pytest tests/test_api.py -v
```

#### Run Tests Matching Pattern
```bash
pytest -k "test_summary" -v
```

### End-to-End Testing

#### Install Playwright
```bash
npx playwright install
```

#### Run E2E Tests
```bash
npm run test:e2e
```

#### Run E2E Tests with UI
```bash
npm run test:e2e -- --ui
```

### Test Coverage Goals

| Component | Target Coverage |
|-----------|-----------------|
| API Endpoints | > 90% |
| Services | > 85% |
| React Components | > 80% |
| Utility Functions | > 95% |

---

## 🚢 Deployment

### Frontend Deployment (Vercel)

#### Option 1: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod
```

#### Option 2: GitHub Integration (Recommended)

1. Push code to GitHub
2. Go to [vercel.com/new](https://vercel.com/new)
3. Import your `clinical-notes-assistant` repository
4. Configure environment variables:

   | Variable | Value |
   |----------|-------|
   | `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` | `pk_live_xxx` |
   | `CLERK_SECRET_KEY` | `sk_live_xxx` |
   | `NEXT_PUBLIC_API_URL` | `https://api.yourdomain.com` |

5. Click **Deploy**

#### Custom Domain Setup

1. Go to **Project Settings** → **Domains**
2. Add your domain (e.g., `clinical-notes.yourdomain.com`)
3. Update DNS records as instructed

---

### Backend Deployment

#### Option 1: Railway (Easiest)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
cd backend
railway init

# Add environment variables
railway variables set OPENAI_API_KEY=sk-xxx
railway variables set CLERK_SECRET_KEY=sk_live_xxx
# ... add other variables

# Deploy
railway up
```

#### Option 2: Docker + AWS ECS

**Step 1: Build Docker Image**

```bash
cd backend

# Build image
docker build -t clinical-notes-api:latest .

# Test locally
docker run -p 8000:8000 --env-file .env clinical-notes-api:latest
```

**Step 2: Push to Amazon ECR**

```bash
# Authenticate with ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag clinical-notes-api:latest \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/clinical-notes-api:latest

# Push image
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/clinical-notes-api:latest
```

**Step 3: Deploy to ECS**

1. Create ECS Cluster
2. Create Task Definition with your image
3. Create Service with Application Load Balancer
4. Configure environment variables in Task Definition

#### Option 3: AWS EC2 (Manual)

**Step 1: Launch EC2 Instance**
- AMI: Ubuntu 22.04 LTS
- Instance Type: t3.small (minimum)
- Security Group: Allow ports 22, 80, 443

**Step 2: Install Dependencies**

```bash
# Connect to instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.10
sudo apt install python3.10 python3.10-venv python3-pip -y

# Install Nginx
sudo apt install nginx -y

# Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx -y
```

**Step 3: Clone and Setup**

```bash
# Clone repository
git clone https://github.com/btholath/clinical-notes-assistant.git
cd clinical-notes-assistant/backend

# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Create .env file
nano .env
# Add your environment variables
```

**Step 4: Configure Gunicorn**

```bash
# Create systemd service file
sudo nano /etc/systemd/system/clinical-notes.service
```

```ini
[Unit]
Description=Clinical Notes Assistant API
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/clinical-notes-assistant/backend
Environment="PATH=/home/ubuntu/clinical-notes-assistant/backend/venv/bin"
EnvironmentFile=/home/ubuntu/clinical-notes-assistant/backend/.env
ExecStart=/home/ubuntu/clinical-notes-assistant/backend/venv/bin/gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable clinical-notes
sudo systemctl start clinical-notes
sudo systemctl status clinical-notes
```

**Step 5: Configure Nginx**

```bash
sudo nano /etc/nginx/sites-available/clinical-notes
```

```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/clinical-notes /etc/nginx/sites-enabled/

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

**Step 6: Setup SSL**

```bash
sudo certbot --nginx -d api.yourdomain.com
```

---

### Docker Compose (Full Stack)

For local development or self-hosted deployment:

```yaml
# docker-compose.yml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8000
      - NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=${CLERK_PUBLISHABLE_KEY}
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - CLERK_SECRET_KEY=${CLERK_SECRET_KEY}
      - CORS_ORIGINS=http://localhost:3000
    volumes:
      - ./backend:/app

  # Optional: PostgreSQL database
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=clinical_notes
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=clinical_notes_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

```bash
# Run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## 🔒 Security Considerations

### HIPAA Compliance Notes

> ⚠️ **Important:** This application is designed with security best practices but may require additional measures for full HIPAA compliance in production environments.

| Consideration | Implementation |
|---------------|----------------|
| **Data Encryption** | All API traffic over HTTPS; consider encryption at rest |
| **Authentication** | Clerk provides secure, auditable authentication |
| **Audit Logging** | Implement logging for all PHI access |
| **Access Controls** | Role-based access via Clerk |
| **Data Retention** | Implement data retention policies |
| **BAA** | Obtain Business Associate Agreements with vendors |

### Security Best Practices

1. **Never commit secrets** - Use environment variables
2. **Rotate API keys** regularly
3. **Enable rate limiting** on API endpoints
4. **Implement request validation** on all inputs
5. **Use HTTPS** everywhere in production
6. **Regular dependency updates** - Run `npm audit` and `pip audit`

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/clinical-notes-assistant.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new features

4. **Run tests**
   ```bash
   npm run test
   cd backend && pytest
   ```

5. **Commit with conventional commits**
   ```bash
   git commit -m "feat: add patient history section"
   git commit -m "fix: resolve date picker timezone issue"
   git commit -m "docs: update API documentation"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Convention

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes (formatting) |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks |

### Code Style

- **Frontend:** ESLint + Prettier (run `npm run lint`)
- **Backend:** Black + Flake8 (run `black . && flake8`)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Biju Tholath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) - The React Framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [OpenAI](https://openai.com/) - AI/ML capabilities
- [Clerk](https://clerk.com/) - Authentication made simple
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- [Vercel](https://vercel.com/) - Deployment platform

---

## 📧 Support

If you have questions or need help:

- 📖 Check the [Documentation](#-usage)
- 🐛 Open an [Issue](https://github.com/btholath/clinical-notes-assistant/issues)
- 💬 Start a [Discussion](https://github.com/btholath/clinical-notes-assistant/discussions)
- 📧 Contact: [LinkedIn](https://www.linkedin.com/in/biju-tholath/)

---

## 🗺️ Roadmap

- [ ] Multi-language support (Spanish, French)
- [ ] Voice-to-text note input
- [ ] Integration with popular EHR systems (Epic, Cerner)
- [ ] Custom prompt templates per specialty
- [ ] Team collaboration features
- [ ] Mobile app (React Native)
- [ ] Offline mode with sync

---

<p align="center">
  <strong>Built with ❤️ for Healthcare Providers</strong>
</p>

<p align="center">
  <a href="https://github.com/btholath">
    <img src="https://img.shields.io/badge/Made%20by-btholath-blue?style=flat-square" alt="Made by btholath" />
  </a>
</p>

<p align="center">
  <a href="#-clinical-notes-assistant">⬆️ Back to Top</a>
</p>
