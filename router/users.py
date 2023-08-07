from fastapi import APIRouter

user = APIRouter()


@user.get("/")
async def root():
    return {"message": "Hello World"}
