import os
from dotenv import load_dotenv
from pathlib import Path
# load .env from project root
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=str(env_path))
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    secret_key: str = os.getenv("SECRET_KEY", "change_me_to_a_random_string")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    jwt_exp_minutes: int = int(os.getenv("JWT_EXP_MINUTES", "60"))
settings = Settings()
