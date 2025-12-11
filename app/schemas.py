from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models import Stage
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: Optional[str] = "candidate"
    company_id: Optional[int] = None
class Login(BaseModel):
    email: EmailStr
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
class JobCreate(BaseModel):
    title: str
    description: Optional[str]
    company_id: int
class JobOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    class Config:
        from_attributes = True
class ApplicationCreate(BaseModel):
    resume_url: Optional[str]
class ApplicationOut(BaseModel):
    id: int
    user_id: int
    job_id: int
    stage: Stage
    created_at: datetime
    class Config:
        from_attributes = True
