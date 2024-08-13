from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.auth.routes import router as auth_router
from src.database import create_db_and_tables
from src.payment.routes import router as payment_router
from src.service.routes import router as service_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="Yuppie Backend", summary="Take-home assignment", lifespan=lifespan)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(payment_router, prefix="/api/v1")
app.include_router(service_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
