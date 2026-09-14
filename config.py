from pathlib import Path
import os
import tempfile


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "change-this-development-key"
    DATABASE_PATH = Path(tempfile.gettempdir()) / "pymaster.db" if os.getenv("VERCEL") else BASE_DIR / "database" / "pymaster.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
