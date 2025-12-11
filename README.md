📌 ATS – Job Application Tracking System (Backend)

A production-style backend that handles job listings, applications, authentication, role-based access, workflow stages, and background processing using Redis + RQ.

🌟 Table of Contents

Features

Architecture Diagram

Tech Stack

Directory Structure

API Overview

Environment Variables

Running the Project

Database Migrations

RQ Worker (Background Jobs)

Postman Collection

Sample Jobs

License

🚀 Features
🔐 Authentication

JWT-based secure login & signup

Password hashing

Token expiration support

🧑‍💼 Role-Based Access Control

candidate — can browse jobs, apply

recruiter — manages jobs & applications

admin — full access

📄 Job & Application Management

Job CRUD

Candidates can apply

Recruiters/Admins can update application stage

🔄 Application Workflow (State Machine)
applied → screening → interview → offer → hired/rejected

📬 Background Jobs (Redis + RQ)

Sends email/notification tasks

Non-blocking operations

Separate worker process

🛢 Database & Migrations (Alembic)

Version-controlled schema

Safe upgrades/downgrades

🏛️ Architecture Diagram
                   ┌───────────────────────┐
                   │       Frontend        │
                   └───────────┬───────────┘
                               │ HTTP/JSON
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │  (app/main.py)       │
                    └───────────┬──────────┘
                                │
         ┌──────────────────────┼────────────────────────┐
         ▼                      ▼                        ▼
 ┌───────────────┐      ┌───────────────┐       ┌─────────────────┐
 │ Authentication │      │ Application   │       │ Background Jobs │
 │   (JWT)        │      │  Workflow     │       │   (RQ Worker)   │
 └───────┬────────┘      └───────┬──────┘       └────────┬────────┘
         │                        │                      │
         ▼                        ▼                      ▼
 ┌───────────────┐       ┌───────────────┐     ┌──────────────────┐
 │   Users Table  │       │ Applications  │     │      Redis        │
 └───────────────┘       └───────────────┘     └──────────────────┘
                     ┌────────────────────────┐
                     │ SQLite (dev.db)        │
                     │ Alembic Migrations     │
                     └────────────────────────┘

🧰 Tech Stack
Component	Technology
Backend Framework	FastAPI
Database	SQLite (dev)
ORM	SQLAlchemy
Migrations	Alembic
Authentication	JWT
Background Processing	Redis + RQ
Server	Uvicorn
📂 Directory Structure
ats-backend/
│── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils/
│   │   └── auth.py
│   └── routes/
│       ├── auth.py
│       ├── jobs.py
│       └── applications.py
│
│── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 574b48de7632_initial.py
│
│── alembic.ini
│── requirements.txt
│── README.md

📘 API Overview
🔐 Auth Routes
Method	Endpoint	Description
POST	/api/auth/signup	Create new user
POST	/api/auth/login	Login & get JWT
💼 Job Routes
Method	Endpoint	Role	Description
GET	/api/jobs/	all	Fetch all jobs
POST	/api/jobs/	recruiter/admin	Create job
📝 Application Routes
Method	Endpoint	Role	Description
POST	/api/jobs/{job_id}/apply	candidate	Apply for job
GET	/api/applications/{id}	recruiter/admin	View application
PATCH	/api/applications/{id}/stage	recruiter/admin	Update stage
🔧 Environment Variables

Create a .env file:

SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./dev.db
REDIS_URL=redis://localhost:6379/0

▶️ Running the Project
1️⃣ Activate virtual environment
.venv\Scripts\activate

2️⃣ Start API server
uvicorn app.main:app --reload

3️⃣ Open API docs

Swagger UI:

http://127.0.0.1:8000/docs

🧱 Database Migrations
Create revision
alembic revision --autogenerate -m "your message"

Apply migration
alembic upgrade head

If DB already exists
alembic stamp head
alembic upgrade head

🧵 RQ Worker (Background Jobs)
Start Redis server
redis-server

Start worker
rq worker default

🧪 Postman Collection

You can quickly test endpoints using a Postman collection:

Import these endpoints manually

Or I can provide a ready Postman JSON file → just say:
“Generate Postman Collection JSON.”

📌 Sample Jobs For Testing
Title	Company	Status
Backend Developer	TechCorp	open
Frontend Engineer	WebWorks	open
Data Analyst	DataPlus	open

Use POST /api/jobs/ to create these if needed.

📄 License

MIT License



This ATS backend implements:

✔ Real-world architecture
✔ State machine logic
✔ Background job queue
✔ Database versioning
✔ Modular clean code
