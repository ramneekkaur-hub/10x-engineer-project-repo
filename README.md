# PromptLab

**Your AI Prompt Engineering Platform**

---

## Project Overview

PromptLab is an internal tool designed for AI engineers to **store, organize, and manage their prompts** at scale. Similar to Postman for APIs, PromptLab provides a professional workspace where teams can collaborate on prompt engineering, version control, and testing.

### Purpose

Build a production-ready, full-stack prompt management system that enables teams to:
- Systematically store and organize prompt templates
- Collaborate on prompt engineering workflows
- Track changes and maintain version history
- Test prompts with sample inputs before deployment
- Scale prompt management across the organization

---

## Features

- 📝 **Prompt Templates** — Store reusable prompts with variable substitution (`{{input}}`, `{{context}}`)
- 📁 **Collections** — Organize prompts into logical groupings
- 🏷️ **Tagging & Search** — Quickly find prompts by tags and keywords
- 📜 **Version History** — Track all changes to prompts over time
- 🧪 **Testing Tools** — Test prompts with sample inputs before production use
- 🔍 **Full API** — RESTful API for programmatic access

---

## Prerequisites

- Python 3.10+
- Node.js 18+ (for Week 4 frontend development)
- Git
- pip (Python package manager)

---

## Installation

### Clone the Repository

```bash
git clone <your-repo-url>
cd promptlab
```

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The API will be available at: **http://localhost:8000**

API documentation: **http://localhost:8000/docs**

---

## Quick Start Guide

### Start the Server

```bash
cd backend
python main.py
```

### Run Tests

```bash
cd backend
pytest tests/ -v
```

---

## Project Structure

```
promptlab/
├── README.md                    # You are here
├── PROJECT_BRIEF.md             # Your assignment details
├── GRADING_RUBRIC.md            # How you'll be graded
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py              # FastAPI routes (has bugs!)
│   │   ├── models.py           # Pydantic models
│   │   ├── storage.py          # In-memory storage
│   │   └── utils.py            # Helper functions
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api.py         # Basic tests
│   │   └── conftest.py         # Test fixtures
│   ├── main.py                 # Entry point
│   └── requirements.txt
│
├── frontend/                    # You'll create this in Week 4
├── specs/                       # You'll create this in Week 2
├── docs/                        # You'll create this in Week 2
└── .github/                     # You'll set up CI/CD in Week 3
```

---

## Your Mission

### 🧪 Experimentation Encouraged!
While we provide guidelines, **you are the engineer**. If you see a better way to solve a problem using AI, do it!
- Want to swap the storage layer for a real database? **Go for it.**
- Want to add Authentication? **Do it.**
- Want to rewrite the API in a different style? **As long as tests pass, you're clear.**

The goal is to learn how to build *better* software *faster* with AI. Don't be afraid to break things and rebuild them better.

### Week 1: Fix the Backend
- Understand this codebase using AI
- Find and fix the bugs
- Implement missing features

### Week 2: Document Everything
- Write proper documentation
- Create feature specifications
- Set up coding standards

### Week 3: Make it Production-Ready
- Write comprehensive tests
- Implement new features with TDD
- Set up CI/CD and Docker

### Week 4: Build the Frontend
- Create a React frontend
- Connect it to the backend
- Polish the user experience

---

## API Endpoints (Current)

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | `/health` | Health check | ✅ Works |
| GET | `/prompts` | List all prompts | ⚠️ Has issues |
| GET | `/prompts/{id}` | Get single prompt | ❌ Bug |
| POST | `/prompts` | Create prompt | ✅ Works |
| PUT | `/prompts/{id}` | Update prompt | ⚠️ Has issues |
| DELETE | `/prompts/{id}` | Delete prompt | ✅ Works |
| GET | `/collections` | List collections | ✅ Works |
| GET | `/collections/{id}` | Get collection | ✅ Works |
| POST | `/collections` | Create collection | ✅ Works |
| DELETE | `/collections/{id}` | Delete collection | ❌ Bug |

---

## Development Setup

### Project Structure

```
promptlab/
├── README.md                    # You are here
├── PROJECT_BRIEF.md             # Assignment details
├── GRADING_RUBRIC.md            # Grading criteria
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py              # FastAPI routes
│   │   ├── models.py           # Pydantic models
│   │   ├── storage.py          # Data storage layer
│   │   └── utils.py            # Helper functions
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api.py         # API tests
│   │   └── conftest.py         # Test fixtures
│   ├── main.py                 # Entry point
│   └── requirements.txt
│
├── frontend/                    # Coming Week 4
├── specs/                       # Coming Week 2
├── docs/                        # Coming Week 2
└── .github/                     # Coming Week 3
```

### Tech Stack

- **Backend**: Python 3.10+, FastAPI, Pydantic
- **Frontend**: React, Vite (Week 4)
- **Testing**: pytest
- **DevOps**: Docker, GitHub Actions (Week 3)

### Development Workflow

1. Create a feature branch from `main`
2. Write tests for new functionality
3. Implement features following the API specification
4. Run tests: `pytest tests/ -v`
5. Submit a pull request with clear description

---

## Contributing Guidelines

### Code Standards

- Follow PEP 8 for Python code
- Use type hints in function signatures
- Write docstrings for all functions and classes
- Keep functions focused and testable

### Commit Messages

Use clear, descriptive commit messages:
```
feat: add prompt search by tags
fix: resolve bug in collection deletion
docs: update API documentation
test: add tests for prompt creation
```

### Testing Requirements

- All new features must include tests
- Maintain or improve code coverage
- Run `pytest tests/ -v` before committing

### Pull Request Process

1. Ensure all tests pass locally
2. Update documentation if needed
3. Write a clear PR description
4. Link related issues
5. Request review from team

---

## AI-Assisted Development

This is an **AI-assisted coding course**. You are encouraged to:
- Use AI tools to understand and refactor code
- Leverage AI for testing and documentation
- Implement improvements beyond the requirements
- Experiment with architectural changes (as long as tests pass)

---

## Resources

- **Assignment Details**: See `PROJECT_BRIEF.md`
- **Grading Criteria**: See `GRADING_RUBRIC.md`
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **pytest Documentation**: https://docs.pytest.org/

---

## Support

- 💬 Ask questions in the course forum
- 📚 Refer to `PROJECT_BRIEF.md` for detailed instructions
- 🤖 Use AI tools effectively for development
- ✅ Check `GRADING_RUBRIC.md` to understand expectations



Good luck, and welcome to the team! 🚀
