import os
from dotenv import load_dotenv # type: ignore
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Aniket@26')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = os.getenv('DATABASE_USER', 'root')
    DB_PASS = os.getenv('DATABASE_PASSWORD', 'Pass@123')
    DB_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
    DB_PORT = os.getenv('DATABASE_PORT', '3306')
    DB_NAME = os.getenv('DATABASE_NAME', 'student_db')
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

