from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql://salastodolist_fastapi_user:TAVWZx6YBTdnFyxRhL0t7wAXuQPOkTq7@dpg-cvtsip7gi27c73aa7j90-a.singapore-postgres.render.com/salastodolist_fastapi"

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_db_connection():
    try:
        db = SessionLocal()
        result = db.execute("SELECT 1")
        print("Database connection test successful:", result.fetchall())
        db.close()
    except SQLAlchemyError as e:
        print("Error connecting to the database:", e)
        db.rollback()

