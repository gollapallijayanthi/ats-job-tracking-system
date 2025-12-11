# 📌 **ATS – Job Application Tracking System (Backend)**

A production-style backend that handles job listings, applications, authentication, role-based access, workflow stages, and background processing using Redis + RQ.

---

## 🌟 **Table of Contents**

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
* [License](#-license)

---

## 🚀 **Features**

### 🔐 Authentication

* JWT-based secure login & signup
* Password hashing
* Token expiration support

### 🧑‍💼 Role-Based Access Control

| Role          | Permissions                |
| ------------- | -------------------------- |
| **candidate** | Browse jobs, apply         |
| **recruiter** | Manage jobs & applications |
| **admin**     | Full access                |

### 📄 Job & Application Management

* Job CRUD
* Candidates can apply
* Recruiters/Admins can update application stage

### 🔄 Application Workflow (State Machine)

```
applied → screening → interview → offer → hired / rejected
```

### 📬 Background Jobs (Redis + RQ)

* Sends email/notification tasks
* Non-blocking operations
* Runs in separate worker process

### 🛢 Database Versioning (Alembic)

* Safe schema migrations
* Version-controlled database

---

## 🏛️ **Architecture Diagram**

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

## 🧰 **Tech Stack**

| Component         | Technology |
| ----------------- | ---------- |
| Backend Framework | FastAPI    |
| Database          | SQLite     |
| ORM               | SQLAlchemy |
| Migrations        | Alembic    |
| Auth              | JWT        |
| Background Jobs   | Redis + RQ |
| Server            | Uvicorn    |

---

## 📂 **Directory Structure**

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

## 📘 **API Overview**

### 🔐 **Auth Routes**

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| POST   | `/api/auth/signup` | Create a new user |
| POST   | `/api/auth/login`  | Login & get JWT   |

---

### 💼 **Job Routes**

| Method | Endpoint     | Role            | Description    |
| ------ | ------------ | --------------- | -------------- |
| GET    | `/api/jobs/` | all             | Fetch all jobs |
| POST   | `/api/jobs/` | recruiter/admin | Create job     |

---

### 📝 **Application Routes**

| Method | Endpoint                       | Role            | Description      |
| ------ | ------------------------------ | --------------- | ---------------- |
| POST   | `/api/jobs/{job_id}/apply`     | candidate       | Apply for job    |
| GET    | `/api/applications/{id}`       | recruiter/admin | View application |
| PATCH  | `/api/applications/{id}/stage` | recruiter/admin | Update stage     |

---

## 🔧 **Environment Variables**

Create a `.env` file:

```
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite:///./dev.db
REDIS_URL=redis://localhost:6379/0
```

---

## ▶️ **Running the Project**

### 1️⃣ Activate virtual environment

```
.venv\Scripts\activate
```

### 2️⃣ Start API server

```
uvicorn app.main:app --reload
```

### 3️⃣ API Documentation

**Swagger UI:**

➡️ [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧱 **Database Migrations**

### Create a new migration

```
alembic revision --autogenerate -m "your message"
```

### Apply migration

```
alembic upgrade head
```

### If DB already exists

```
alembic stamp head
alembic upgrade head
```

---

## 🧵 **RQ Worker (Background Jobs)**

### Start Redis

```
redis-server
```

### Start Worker

```
rq worker default
```

---

## 🧪 **Postman Collection**

You can test all endpoints easily using Postman.

If you want a *ready-made Postman JSON* just say:

👉 **"Generate Postman Collection JSON"**

---

## 📌 **Sample Jobs For Testing**

| Title             | Company  | Status |
| ----------------- | -------- | ------ |
| Backend Developer | TechCorp | open   |
| Frontend Engineer | WebWorks | open   |
| Data Analyst      | DataPlus | open   |

Run using:

```
POST /api/jobs/
```

---

## 📄 **License**

This project is licensed under the **MIT License**.

---

## 🎉 Final Notes

This ATS backend includes:

✔ Real-world architecture
✔ State machine logic
✔ Background job queue
✔ Database versioning
✔ Modular clean code


