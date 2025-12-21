TaskForge

TaskForge is a service-oriented backend API for managing projects and tasks within an organization.
It is designed to demonstrate clean backend architecture, explicit domain modeling, and reliable data handling using Python and FastAPI.

This project intentionally focuses on backend fundamentals rather than UI or authentication complexity.

Features

Project management

Task creation and assignment

Enum-backed task status (todo, in_progress, done)

Controlled task status updates

Relational data integrity via PostgreSQL

Clean OpenAPI / Swagger documentation

Service-layer architecture

Tech Stack

Python 3.12

FastAPI – API framework

PostgreSQL – relational database

SQLAlchemy 2.0 – ORM

Alembic – database migrations

Pydantic v2 – request/response validation

Architecture Overview

TaskForge follows a layered, service-oriented design:

app/
├── api/ # HTTP routes (FastAPI)
│ └── v1/
├── services/ # Business logic
├── models/ # SQLAlchemy ORM models
├── schemas/ # Pydantic schemas
├── db/ # DB session and base
└── main.py # Application entrypoint

Key principles

Thin routes: API routes only handle HTTP concerns

Service layer: All business logic lives in services

Explicit domain modeling: Enums, foreign keys, and constraints are enforced at the database level

Migrations first: Schema changes are handled via Alembic, not runtime magic

Task Status Design

Tasks use a PostgreSQL-backed enum for status:

todo
in_progress
done

This ensures:

Only valid states are stored

API and database remain consistent

Invalid transitions fail early

Status updates are handled via a dedicated PATCH endpoint:

PATCH /api/v1/tasks/{task_id}/status

Running Locally
Prerequisites

Python 3.12+

PostgreSQL

Virtual environment recommended

Setup

git clone https://github.com/your-username/taskforge.git

cd taskforge
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt

Database

Create a PostgreSQL database named taskforge and configure your connection string via environment variables.

Run migrations:

alembic upgrade head

Start the API

uvicorn app.main:app --reload

Visit Swagger UI:

http://127.0.0.1:8000/docs

Example Workflow (Swagger)

Create a project

Create tasks for that project

Update task status via PATCH

List tasks by project

All interactions return clean JSON and validated enum values.
