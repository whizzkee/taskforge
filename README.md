# 🛠 TaskForge

[![FastAPI](https://img.shields.io/badge/API-FastAPI-05998b?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![SQLAlchemy 2.0](https://img.shields.io/badge/ORM-SQLAlchemy_2.0-red?style=flat-square)](https://www.sqlalchemy.org/)

**TaskForge** is a production-ready backend service designed with a **Domain-Driven Design (DDD)** mindset. While many projects focus on simple CRUD operations, TaskForge is built to demonstrate **Service Layer patterns**, **Atomic state transitions**, and **Relational Data Integrity**.

> [!IMPORTANT]
> **Architectural Goal:** This project demonstrates the separation of HTTP concerns from business logic, ensuring the core domain remains testable, scalable, and database-agnostic.

---

## 🏛 Architecture & Data Flow

TaskForge utilizes a **Layered Architecture** to prevent "Fat Routes" and ensure a clean separation of concerns. This structure makes the codebase easier to navigate, test, and maintain as complexity grows.



### The Request Lifecycle:
1.  **API Layer (`app/api`):** Handles serialization, HTTP status codes, and Pydantic validation. It acts as the protocol gatekeeper.
2.  **Service Layer (`app/services`):** The "Brain" of the application. It orchestrates business rules (e.g., verifying project status before allowing task creation).
3.  **Data Layer (`app/models`):** SQLAlchemy 2.0 models using Type-Annotated mapping for strict type safety and better IDE support.

---

## 🧱 Project Structure

```text
app/
├── api/v1/          # Protocol Layer (FastAPI routes & Dependencies)
├── services/        # Business Logic Layer (Domain rules & Orchestration)
├── models/          # Persistence Layer (SQLAlchemy 2.0 Mappings)
├── schemas/         # Validation Layer (Pydantic v2 BaseModels)
├── db/              # Database Engine configuration & Session management
└── main.py          # Application Factory & Middleware setup
🛡 Key Technical Decisions1. Explicit State ManagementInstead of allowing arbitrary string updates for task statuses, I implemented a PostgreSQL-backed Enum. This ensures that the database remains the "Source of Truth," preventing invalid states even if the database is accessed outside of the API.2. SQLAlchemy 2.0 "Style"I leverage the latest SQLAlchemy 2.0 syntax, specifically Mapped and mapped_column. This allows mypy and other static analysis tools to catch attribute errors during development rather than at runtime.3. Service Pattern for DecouplingBy isolating business logic into services/, the application is prepared for future transitions—such as moving from REST to GraphQL or adding a CLI interface—without needing to rewrite core logic.📡 API SpecificationThe API is fully documented via OpenAPI. Once the server is running, visit /docs for the interactive Swagger UI.MethodEndpointDescriptionGET/projectsList all projects with paginationPOST/tasksCreate task with relational validationPATCH/tasks/{id}/statusAtomic status transitionExample Atomic Status Update:JSON// PATCH /api/v1/tasks/42/status
{
  "status": "in_progress"
}
🚀 Development Setup1. Environment ConfigurationBashgit clone [https://github.com/trevor-dev-johnson/taskforge.git](https://github.com/trevor-dev-johnson/taskforge.git)
cd taskforge
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
2. Database Migrations (Alembic)This project follows a "Migrations-First" workflow to ensure schema consistency across environments.Bash# Configure your DATABASE_URL in environment variables
export DATABASE_URL="postgresql://user:pass@localhost:5432/taskforge"
alembic upgrade head
3. ExecutionBashuvicorn app.main:app --reload
🔍 Future Roadmap[ ] Unit Testing Suite: Implement comprehensive testing using pytest and an isolated test database.[ ] Structured Logging: Integrate structlog for production-grade observability and ELK-stack compatibility.[ ] Background Workers: Add Celery or ARQ for handling long-running reporting tasks.Contact & PortfolioPortfolio: trevorjohnson.devLinkedIn: linkedin.com/in/trevor-johnson-dev
