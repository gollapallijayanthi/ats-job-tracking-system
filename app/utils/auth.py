from typing import Optional
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config import settings
from app.db import SessionLocal
from app import crud, models
bearer = HTTPBearer()
def create_access_token(subject: str, role: str, expires_minutes: int = None) -> str:
    from datetime import datetime, timedelta
    exp = datetime.utcnow() + timedelta(minutes=(expires_minutes or settings.jwt_exp_minutes))
    payload = {"sub": str(subject), "role": role, "exp": exp}
    token = jwt.encode(payload, settings.secret_key, algorithm=settings.jwt_algorithm)
    return token
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def get_current_user(creds: HTTPAuthorizationCredentials = Depends(bearer), db=Depends(get_db)) -> models.User:
    token = creds.credentials
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    user = db.get(models.User, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
