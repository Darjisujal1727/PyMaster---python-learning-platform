from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "change-this-development-key"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'database' / 'pymaster.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
