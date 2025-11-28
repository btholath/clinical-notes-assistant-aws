<p align="center">
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Clerk-6C47FF?style=for-the-badge&logo=clerk&logoColor=white" alt="Clerk" />
</p>

<h1 align="center">🚀 AI SaaS Boilerplate</h1>

<p align="center">
  <strong>A production-ready full-stack AI SaaS application built with Next.js and FastAPI</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#testing">Testing</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## 📋 Overview

This is a comprehensive AI SaaS boilerplate that provides everything you need to build and launch your own AI-powered Software-as-a-Service application. It combines the power of Next.js for the frontend with FastAPI for the backend, featuring real-time AI response streaming, secure authentication via Clerk, and integrated subscription management.

## ✨ Features

- **🤖 Real-time AI Streaming** - Stream AI responses in real-time for a seamless user experience
- **🔐 Authentication** - Secure user authentication powered by Clerk
- **💳 Subscription Management** - Built-in subscription and billing features
- **⚡ Full-stack TypeScript/Python** - Type-safe development across the entire stack
- **🎨 Modern UI** - Clean, responsive interface built with React
- **📱 Responsive Design** - Works seamlessly across desktop and mobile devices
- **🔄 Hot Reload** - Fast development with automatic page updates

## 🛠 Tech Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| [Next.js](https://nextjs.org/) | React framework with SSR/SSG |
| [TypeScript](https://www.typescriptlang.org/) | Type-safe JavaScript |
| [React](https://reactjs.org/) | UI component library |
| [Tailwind CSS](https://tailwindcss.com/) | Utility-first CSS framework |

### Backend
| Technology | Purpose |
|------------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | High-performance Python API framework |
| [Python 3.10+](https://www.python.org/) | Backend programming language |
| [Pydantic](https://pydantic-docs.helpmanual.io/) | Data validation |

### Services & Infrastructure
| Technology | Purpose |
|------------|---------|
| [Clerk](https://clerk.com/) | Authentication & user management |
| [Stripe](https://stripe.com/) | Payment processing (optional) |
| [Vercel](https://vercel.com/) | Frontend deployment |
| [AWS/Railway](https://railway.app/) | Backend deployment |

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18.0.0 or higher)
  ```bash
  node --version
  ```
- **npm** or **yarn** or **pnpm**
  ```bash
  npm --version
  ```
- **Python** (v3.10 or higher)
  ```bash
  python --version
  ```
- **pip** (Python package manager)
  ```bash
  pip --version
  ```
- **Git**
  ```bash
  git --version
  ```

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/btholath/saas.git
cd saas
```

### Step 2: Frontend Setup

#### 2.1 Install Node.js Dependencies

```bash
npm install
# or
yarn install
# or
pnpm install
```

#### 2.2 Configure Environment Variables

Create a `.env.local` file in the root directory:

```bash
cp .env.example .env.local
```

Add your environment variables:

```env
# Clerk Authentication
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxx
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxx
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/dashboard
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/dashboard

# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000

# Stripe (Optional - for subscriptions)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx
```

#### 2.3 Run the Development Server

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

### Step 3: Backend Setup (FastAPI)

#### 3.1 Create and Activate Virtual Environment

```bash
# Navigate to backend directory (if separate)
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
```

#### 3.2 Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 3.3 Configure Backend Environment Variables

Create a `.env` file in the backend directory:

```env
# Application
APP_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/saas_db

# Clerk
CLERK_SECRET_KEY=sk_test_xxxxxxxxxxxxx

# OpenAI / AI Provider
OPENAI_API_KEY=sk-xxxxxxxxxxxxx

# Stripe
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx

# CORS
CORS_ORIGINS=http://localhost:3000
```

#### 3.4 Run the FastAPI Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000).

API documentation is auto-generated at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📁 Project Structure

```
saas/
├── 📂 pages/                    # Next.js pages (file-based routing)
│   ├── 📂 api/                  # API routes
│   │   └── hello.ts             # Example API endpoint
│   ├── _app.tsx                 # App wrapper component
│   ├── _document.tsx            # Custom document
│   ├── index.tsx                # Home page
│   ├── product.tsx              # Product page
│   ├── sign-in/[[...index]].tsx # Clerk sign-in page
│   ├── sign-up/[[...index]].tsx # Clerk sign-up page
│   └── dashboard.tsx            # User dashboard
│
├── 📂 components/               # Reusable React components
│   ├── 📂 ui/                   # UI primitives
│   ├── Header.tsx               # Navigation header
│   ├── Footer.tsx               # Footer component
│   └── ...
│
├── 📂 styles/                   # Global styles
│   └── globals.css              # Global CSS/Tailwind imports
│
├── 📂 lib/                      # Utility functions & configurations
│   ├── api.ts                   # API client utilities
│   └── utils.ts                 # Helper functions
│
├── 📂 hooks/                    # Custom React hooks
│   └── useAuth.ts               # Authentication hook
│
├── 📂 public/                   # Static assets
│   ├── favicon.ico
│   └── images/
│
├── 📂 backend/                  # FastAPI backend (if monorepo)
│   ├── 📂 app/
│   │   ├── 📂 api/              # API endpoints
│   │   ├── 📂 models/           # Database models
│   │   ├── 📂 services/         # Business logic
│   │   └── 📂 core/             # Core configurations
│   ├── main.py                  # FastAPI application entry
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # Backend environment variables
│
├── .env.local                   # Frontend environment variables
├── .env.example                 # Example environment template
├── .gitignore                   # Git ignore rules
├── next.config.js               # Next.js configuration
├── tailwind.config.js           # Tailwind CSS configuration
├── tsconfig.json                # TypeScript configuration
├── package.json                 # Node.js dependencies
└── README.md                    # This file
```

## ⚙️ Configuration

### Clerk Authentication Setup

1. **Create a Clerk Account**
   - Go to [clerk.com](https://clerk.com) and sign up
   - Create a new application

2. **Get API Keys**
   - Navigate to your application dashboard
   - Copy the **Publishable Key** and **Secret Key**
   - Add them to your `.env.local` file

3. **Configure Sign-in/Sign-up URLs**
   - In Clerk Dashboard, go to **Paths**
   - Set the following:
     - Sign-in URL: `/sign-in`
     - Sign-up URL: `/sign-up`
     - After sign-in URL: `/dashboard`
     - After sign-up URL: `/dashboard`

### Stripe Subscription Setup (Optional)

1. **Create a Stripe Account**
   - Go to [stripe.com](https://stripe.com) and sign up

2. **Get API Keys**
   - Navigate to **Developers** → **API Keys**
   - Copy the **Publishable Key** and **Secret Key**

3. **Set Up Products and Prices**
   - Go to **Products** in Stripe Dashboard
   - Create subscription products with pricing tiers

4. **Configure Webhooks**
   - Go to **Developers** → **Webhooks**
   - Add endpoint: `https://yourdomain.com/api/webhooks/stripe`
   - Select events: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`

### AI Provider Configuration

Add your AI provider API key to the backend `.env`:

```env
# OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxx

# Or Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# Or other providers as needed
```

## 🧪 Testing

### Frontend Testing

```bash
# Run unit tests
npm run test

# Run tests with coverage
npm run test:coverage

# Run tests in watch mode
npm run test:watch
```

### Backend Testing

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate

# Run tests with pytest
pytest

# Run tests with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api.py -v
```

### End-to-End Testing

```bash
# Install Playwright (if using)
npx playwright install

# Run E2E tests
npm run test:e2e
```

## 🚢 Deployment

### Frontend Deployment (Vercel)

#### Option 1: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Deploy to production
vercel --prod
```

#### Option 2: Deploy via GitHub Integration

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click **New Project**
4. Import your GitHub repository
5. Configure environment variables in Vercel dashboard
6. Click **Deploy**

**Required Environment Variables in Vercel:**
- `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
- `CLERK_SECRET_KEY`
- `NEXT_PUBLIC_API_URL`
- `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` (if using Stripe)
- `STRIPE_SECRET_KEY` (if using Stripe)

### Backend Deployment (Railway/AWS)

#### Option 1: Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

#### Option 2: AWS (EC2/ECS)

1. **Create an EC2 Instance or ECS Cluster**

2. **Install Dependencies on Server**
   ```bash
   sudo apt update
   sudo apt install python3.10 python3.10-venv nginx
   ```

3. **Clone and Setup**
   ```bash
   git clone https://github.com/btholath/saas.git
   cd saas/backend
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
   ```

5. **Configure Nginx Reverse Proxy**
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
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

6. **Set Up SSL with Certbot**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d api.yourdomain.com
   ```

#### Option 3: Docker Deployment

Create a `Dockerfile` in the backend directory:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
# Build image
docker build -t saas-backend .

# Run container
docker run -d -p 8000:8000 --env-file .env saas-backend
```

## 📝 API Documentation

Once the backend is running, access the auto-generated API documentation:

| Documentation | URL |
|--------------|-----|
| Swagger UI | [http://localhost:8000/docs](http://localhost:8000/docs) |
| ReDoc | [http://localhost:8000/redoc](http://localhost:8000/redoc) |
| OpenAPI JSON | [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) |

## 🔧 Available Scripts

### Frontend (npm/yarn/pnpm)

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run test` | Run tests |

### Backend (Python)

| Command | Description |
|---------|-------------|
| `uvicorn main:app --reload` | Start development server |
| `pytest` | Run tests |
| `black .` | Format code |
| `flake8` | Lint code |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/btholath/saas.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests for new features

4. **Commit Your Changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   
   Follow [Conventional Commits](https://www.conventionalcommits.org/) specification.

5. **Push to Your Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Describe your changes
   - Link any related issues
   - Request review from maintainers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) - The React Framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Clerk](https://clerk.com/) - Authentication made simple
- [Vercel](https://vercel.com/) - Deployment platform

## 📧 Support

If you have any questions or need help, please:

- Open an [Issue](https://github.com/btholath/saas/issues)
- Start a [Discussion](https://github.com/btholath/saas/discussions)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/btholath">btholath</a>
</p>

<p align="center">
  <a href="#top">⬆️ Back to Top</a>
</p>
