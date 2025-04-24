from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://salastodolist_fastapi_user:TAVWZx6YBTdnFyxRhL0t7wAXuQPOkTq7@dpg-cvtsip7gi27c73aa7j90-a.singapore-postgres.render.com/salastodolist_fastapi"
SQLALCHEMY_DATABASE_URL = "postgresql://salastodolist_fastapi_user:TAVWZx6YBTdnFyxRhL0t7wAXuQPOkTq7@dpg-cvtsip7gi27c73aa7j90-a.singapore-postgres.render.com/salastodolist_fastapi"

engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

