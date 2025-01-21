from fastapi import FastAPI

from repository.db import startup
from routers import user_router

startup()
app = FastAPI()
app.include_router(user_router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}
