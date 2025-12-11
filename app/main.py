from fastapi import FastAPI
from app.routes import auth, jobs, applications
app = FastAPI(title="ATS Backend (dev)")
# NOTE: We DO NOT call Base.metadata.create_all() here when using Alembic.
# Alembic manages the schema via migrations.
# If you want to quickly create tables for experiments, run:
#   from app.db import Base, engine
#   Base.metadata.create_all(bind=engine)
# manually from a short script.
app.include_router(auth.router, prefix="/api/auth")
app.include_router(jobs.router, prefix="/api")
app.include_router(applications.router, prefix="/api")
