from fastapi import FastAPI

from src.auth.routes import router as auth_router
from src.database import create_db_and_tables

app = FastAPI(title="Yuppie Backend", summary="Take-home assignment")
app.include_router(auth_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    create_db_and_tables()
    uvicorn.run(app="src.main:app")
