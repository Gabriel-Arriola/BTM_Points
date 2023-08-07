from fastapi import APIRouter

point = APIRouter(prefix="/point",)


@point.get("/")
async def root():
    return {"message": "Hello World POINT"}
