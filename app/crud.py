from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
# Use pbkdf2_sha256 to avoid bcrypt issues (no 72-byte limit)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
def create_user(db: Session, user_in: schemas.UserCreate):
    hashed = hash_password(user_in.password)
    user = models.User(
        email=user_in.email,
        hashed_password=hashed,
        full_name=user_in.full_name,
        role=user_in.role,
        company_id=user_in.company_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
def create_job(db: Session, job_in: schemas.JobCreate, created_by_id: int):
    job = models.Job(company_id=job_in.company_id, title=job_in.title, description=job_in.description)
    db.add(job); db.commit(); db.refresh(job)
    return job
def create_application(db: Session, user_id: int, job_id: int, resume_url: str | None = None):
    app = models.Application(user_id=user_id, job_id=job_id, resume_url=resume_url)
    db.add(app); db.commit(); db.refresh(app)
    return app
def get_application(db: Session, app_id: int):
    return db.get(models.Application, app_id)
