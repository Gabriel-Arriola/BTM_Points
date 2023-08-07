from fastapi import APIRouter, Response, HTTPException
from typing import List
from starlette.status import HTTP_201_CREATED
from sqlmodel import Session, select
from config.db import engine
from model.users import Users, UserBase
from werkzeug.security import generate_password_hash

user = APIRouter(prefix="/user", )


@user.get("/", response_model=List[Users])
async def get_users():
    with Session(engine) as session:
        result = session.exec(select(Users)).fetchall()
        return result


@user.get("/{user_id}", response_model=Users)
async def get_user_by_id(user_id: int):
    with Session(engine) as session:
        result = session.get(Users, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result


@user.post("/", status_code=HTTP_201_CREATED)
async def create_user(data_user: UserBase):
    with Session(engine) as session:
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 30)
        session.add(Users(name=new_user["name"], email=new_user["email"], password=new_user["password"]))
        session.commit()
        return Response(status_code=HTTP_201_CREATED)

@user.put("/{user_id}", response_model=Users)
async def update_user(user_id: int, user: UserBase):
    pass
