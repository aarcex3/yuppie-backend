"""Database module"""

from sqlmodel import Session, SQLModel, create_engine

from src.config import SETTINGS

engine = create_engine(f"{SETTINGS.DB_URL}", echo=True)


def create_db_and_tables():
    """
    Init the db engine
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get database session"""

    with Session(engine) as session:
        yield session
    engine.dispose()
