from fastapi import FastAPI

from database.database import init_db
from contextlib import asynccontextmanager
from routers.AuthRouter import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Auth REST Gateway",
    description="Gateway to authentication and authorization",
    version="1.0.0",
    root_path="/auth_rest",
)

app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
