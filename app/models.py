from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text
from datetime import datetime
import enum
from app.db import Base
class Role(str, enum.Enum):
    candidate = "candidate"
    recruiter = "recruiter"
    hiring_manager = "hiring_manager"
    admin = "admin"
class JobStatus(str, enum.Enum):
    open = "open"
    closed = "closed"
class Stage(str, enum.Enum):
    applied = "applied"
    screening = "screening"
    interview = "interview"
    offer = "offer"
    hired = "hired"
    rejected = "rejected"
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String(200))
    role = Column(Enum(Role), nullable=False, default=Role.candidate)
    company_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(Enum(JobStatus), default=JobStatus.open)
    created_at = Column(DateTime, default=datetime.utcnow)
class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    stage = Column(Enum(Stage), default=Stage.applied)
    resume_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
class ApplicationHistory(Base):
    __tablename__ = "application_history"
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)
    from_stage = Column(Enum(Stage))
    to_stage = Column(Enum(Stage))
    changed_by = Column(Integer, ForeignKey("users.id"))
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
