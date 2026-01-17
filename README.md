🛠 TaskForgeTaskForge is a production-ready backend skeleton designed with a Domain-Driven Design (DDD) mindset. While many junior projects focus on "CRUD," TaskForge focuses on Service Layer patterns and Relational Integrity.[!IMPORTANT]Architectural Goal: This project demonstrates the separation of HTTP concerns from business logic, ensuring the core domain is testable and database-agnostic.🏛 Architecture & Data FlowTaskForge utilizes a Layered Architecture to prevent the "Fat Controller" (or Fat Route) anti-pattern.The Request Lifecycle:API Layer (app/api): Handles serialization, status codes, and Pydantic validation. It never touches the database directly.Service Layer (app/services): The "Brain." It orchestrates business rules (e.g., "Can this task move to 'Done' if the project is archived?").Data Layer (app/models): SQLAlchemy 2.0 models using Type-Annotated mapping for maximum IDE support and type safety.🧱 Project StructurePlaintextapp/
├── api/v1/          # Protocol Layer (FastAPI routes & Dependencies)
├── services/        # Logic Layer (Business rules & Orchestration)
├── models/          # Persistence Layer (SQLAlchemy 2.0 Mappings)
├── schemas/         # Validation Layer (Pydantic v2 BaseModels)
├── db/              # Engine configuration & Session management
└── main.py          # App Factory & Middleware setup
🛡 Key Technical Decisions1. Explicit State ManagementInstead of allowing arbitrary string updates, I implemented a PostgreSQL-backed Enum for Task Status. This ensures that the database remains the "Source of Truth," preventing data corruption even if a script bypasses the API.2. SQLAlchemy 2.0 "Style"I leverage Mapped and mapped_column for strict typing. This allows mypy to catch attribute errors during development rather than at runtime.3. Service Pattern for DecouplingBy isolating business logic into services/, the application is prepared for a future shift—for example, moving from a REST API to a GraphQL interface or a CLI tool—without rewriting the core task management logic.📡 API Specification (Brief)The API is fully documented via OpenAPI. Once running, visit /docs.MethodEndpointDescriptionGET/projectsList all projects with paginationPOST/tasksCreate task with relational validationPATCH/tasks/{id}/statusAtomic status transitionExample Atomic Status Update:JSON// PATCH /api/v1/tasks/42/status
{
  "status": "in_progress"
}
🚀 Development Setup1. Environment ConfigurationBashgit clone https://github.com/trevor-dev-johnson/taskforge.git
cd taskforge
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
2. Database Migrations (Alembic)This project uses a "Migrations-First" workflow.Bashexport DATABASE_URL="postgresql://user:pass@localhost:5432/taskforge"
alembic upgrade head
3. ExecutionBashuvicorn app.main:app --reload
🔍 Future Roadmap[ ] Unit Testing Suite: Implement pytest with a refreshed Docker-based test database.[ ] Structured Logging: Replace standard prints with structlog for ELK-stack compatibility.[ ] Background Workers: Integrate Celery for heavy reporting tasks.Contact & PortfolioPortfolio: trevorjohnson.devLinkedIn: linkedin.com/in/trevor-johnson-dev
