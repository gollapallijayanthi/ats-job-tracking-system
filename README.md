# **ATS – Job Application Tracking System (Backend)**

A production-grade backend API for managing job listings, user authentication, applications, role-based permissions, workflow stages, and background job processing using Redis + RQ.
Designed with clean architecture, database migrations, and scalable patterns used in real-world ATS systems.

---

## **Table of Contents**

* [Features](#-features)
* [Architecture Diagram](#-architecture-diagram)
* [Tech Stack](#-tech-stack)
* [Directory Structure](#-directory-structure)
* [API Overview](#-api-overview)
* [Environment Variables](#-environment-variables)
* [Running the Project](#-running-the-project)
* [Database Migrations](#-database-migrations)
* [RQ Worker (Background Jobs)](#-rq-worker-background-jobs)
* [Postman Collection](#-postman-collection)
* [Sample Jobs](#-sample-jobs-for-testing)
* [Screenshots](#-screenshots-optional)
* [License](#-license)

---

##  **Features**

###  Authentication

* JWT-based secure login & signup
* Password hashing
* Token expiration support

###  Role-Based Access Control

| Role          | Permissions                |
| ------------- | -------------------------- |
| **candidate** | Browse jobs, apply         |
| **recruiter** | Manage jobs & applications |
| **admin**     | Full access                |

###  Job & Application Management

* Create, list, and manage jobs
* Candidates can apply for jobs
* Recruiters/Admins can update application stage

###  Application Workflow (State Machine)

```
applied → screening → interview → offer → hired / rejected
```

###  Background Jobs (Redis + RQ)

* Runs notification/email tasks
* Non-blocking heavy operations
* Worker service runs separately

###  Database Versioning (Alembic)

* All schema changes tracked
* Safe upgrades/downgrades

---

##  **Architecture Diagram**

```
                   ┌───────────────────────┐
                   │        Frontend       │
                   └───────────┬───────────┘
                               │ HTTP/JSON
                               ▼
                    ┌──────────────────────┐
                    │        FastAPI       │
                    │     (main app)       │
                    └───────────┬──────────┘
                                │
     ┌──────────────────────────┼───────────────────────────┐
     ▼                          ▼                           ▼
┌──────────────┐       ┌────────────────┐         ┌────────────────────┐
│ Authentication│       │ Application    │         │   Background Jobs  │
│    (JWT)      │       │   Workflow     │         │     (RQ Worker)    │
└───────┬───────┘       └───────┬────────┘         └──────────┬─────────┘
        │                       │                             │
        ▼                       ▼                             ▼
┌──────────────┐       ┌────────────────┐          ┌────────────────────┐
│   Users DB   │       │ Applications DB│          │       Redis         │
└──────────────┘       └────────────────┘          └────────────────────┘

             ┌──────────────────────────────────────────┐
             │              SQLite (dev.db)              │
             │           Alembic Migrations              │
             └──────────────────────────────────────────┘
```

---

##  **Tech Stack**

| Component         | Technology |
| ----------------- | ---------- |
| Backend Framework | FastAPI    |
| Database          | SQLite     |
| ORM               | SQLAlchemy |
| Migrations        | Alembic    |
| Authentication    | JWT        |
| Background Jobs   | Redis + RQ |
| Server            | Uvicorn    |

---

##  **Directory Structure**

```
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
```

---

##  **API Overview**

###  Auth Routes

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| POST   | `/api/auth/signup` | Create a new user |
| POST   | `/api/auth/login`  | Login & get JWT   |

---

###  Job Routes

| Method | Endpoint     | Role            | Description    |
| ------ | ------------ | --------------- | -------------- |
| GET    | `/api/jobs/` | all             | Fetch all jobs |
| POST   | `/api/jobs/` | recruiter/admin | Create job     |

---

###  Application Routes

| Method | Endpoint                       | Role            | Description      |
| ------ | ------------------------------ | --------------- | ---------------- |
| POST   | `/api/jobs/{job_id}/apply`     | candidate       | Apply for job    |
| GET    | `/api/applications/{id}`       | recruiter/admin | View application |
| PATCH  | `/api/applications/{id}/stage` | recruiter/admin | Update stage     |

---

##  **Environment Variables**

Create a `.env` file in project root:

```
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./dev.db
REDIS_URL=redis://localhost:6379/0
```

---

##  **Running the Project**

### 1️ Activate virtual environment

```
.venv\Scripts\activate
```

### 2️ Install dependencies

```
pip install -r requirements.txt
```

### 3️ Start the server

```
uvicorn app.main:app --reload
```

### 4️ API Documentation (Swagger)

 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

##  **Database Migrations**

### Create a new migration

```
alembic revision --autogenerate -m "your message"
```

### Apply all migrations

```
alembic upgrade head
```

### If DB already exists

```
alembic stamp head
alembic upgrade head
```

---

##  **RQ Worker (Background Jobs)**

### Start Redis

```
redis-server
```

### Start worker

```
rq worker default
```

---



##  **Postman Collection**

A complete Postman collection is included in the repository.

 **Direct File Link:**
 **[ATS-Backend-Collection.json](https://github.com/gollapallijayanthi/ats-job-tracking-system/blob/main/ATS-Backend-Collection.json)**

You can import this file directly into Postman to test all API endpoints:

✔ Signup
✔ Login
✔ Create Jobs
✔ Apply for Jobs
✔ Update Application Stage
✔ View Applications

---





##  **Sample Jobs For Testing**

| Title             | Company  | Status |
| ----------------- | -------- | ------ |
| Backend Developer | TechCorp | open   |
| Frontend Engineer | WebWorks | open   |
| Data Analyst      | DataPlus | open   |

Create via:

```
POST /api/jobs/
```

---

##  **Screenshots (Optional)**

You may include screenshots such as:

* Swagger UI
* Postman results
* Application workflow

*(Add your images here when available.)*

---

##  **License**

This project is licensed under the **MIT License**.

---

##  Final Notes

This ATS backend demonstrates:

* Real-world architecture
* Workflow/state machine logic
* Background job queues
* Database migration discipline
* Clean modular code
