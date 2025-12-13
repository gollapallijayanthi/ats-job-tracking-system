from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app import crud, schemas
from app.models import Job  

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs", response_model=schemas.JobOut)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job, created_by_id=0)

@router.get("/jobs/{job_id}", response_model=schemas.JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(Job, job_id)   
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
