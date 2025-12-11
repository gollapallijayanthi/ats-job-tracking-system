from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app import crud, schemas
from app.utils.auth import create_access_token
from datetime import datetime, timedelta
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/register", response_model=dict)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = crud.create_user(db, user)
    return {"id": created.id, "email": created.email, "role": created.role}
@router.post("/login", response_model=schemas.Token)
def login(form_data: schemas.Login, db: Session = Depends(get_db)):
    email = form_data.email
    password = form_data.password
    user = crud.get_user_by_email(db, email)
    if not user or not crud.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(subject=str(user.id), role=user.role)
    return {"access_token": token, "token_type":"bearer"}
