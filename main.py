from fastapi import FastAPI
from router.users import user
from router.points import point

app = FastAPI()

app.include_router(user)
app.include_router(point)


'''
@app.get("/a")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
'''