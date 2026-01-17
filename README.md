# 🛠 TaskForge

[![FastAPI](https://img.shields.io/badge/API-FastAPI-05998b?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://www.python.org/)

**TaskForge** is a robust backend service designed with a **Layered Architecture** to manage organizational projects and complex task workflows. 

Rather than a simple CRUD app, TaskForge serves as a blueprint for production-grade API design, focusing on **decoupled business logic**, **strict domain modeling**, and **database-enforced invariants**.

---

## 🏛 Architectural Pattern

TaskForge follows a strict separation of concerns to ensure the system is easy to test and extend.



* **API Layer (FastAPI):** Handles protocol-level concerns, request validation, and serialization. It acts as the entry point, ensuring only valid data reaches the internal logic.
* **Service Layer:** The core "brain" of the application where all business rules and domain logic are isolated. This decoupling allows the logic to be tested independently of the framework.
* **Persistence Layer (Postgres + SQLAlchemy):** Manages relational integrity and migration-driven schema evolution via Alembic. It enforces data constraints at the engine level to ensure a consistent state.

---

## 🛡 Key Technical Decisions

* **Database-Enforced Invariants:** I utilize PostgreSQL constraints and Enums to ensure that the data remains valid even if accessed outside the application layer.
* **Type-Safe Domain Modeling:** Leveraging Pydantic v2 and SQLAlchemy 2.0's `Mapped` types to catch potential bugs during development rather than at runtime.
* **Clean Dependency Injection:** Using FastAPI's dependency system to manage database sessions and service instances, making the code highly modular.
