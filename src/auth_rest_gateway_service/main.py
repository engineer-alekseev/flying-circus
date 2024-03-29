from fastapi import FastAPI


from routers.AuthRouter import AuthRouter

app = FastAPI(
    title="Auth REST Gateway",
    description="Gateway to authentication and authorization",
    version="1.0.0",
    root_path="/auth_rest",
)

app.include_router(AuthRouter().router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
