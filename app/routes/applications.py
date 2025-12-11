from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import crud, schemas
from app.utils.auth import get_current_user
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/jobs/{job_id}/apply", response_model=schemas.ApplicationOut)
def apply(job_id: int, payload: schemas.ApplicationCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # current_user is the authenticated candidate
    created = crud.create_application(db, user_id=current_user.id, job_id=job_id, resume_url=payload.resume_url)
    return created
@router.get("/applications/{app_id}", response_model=schemas.ApplicationOut)
def get_app(app_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    app_obj = crud.get_application(db, app_id)
    if not app_obj:
        raise HTTPException(404, "Not found")
    # allow owner or recruiter/hiring_manager/admin
    if app_obj.user_id != current_user.id and current_user.role not in ("recruiter", "hiring_manager", "admin"):
        raise HTTPException(403, "Forbidden")
    return app_obj
