from typing import Optional
from sqlmodel import Field, SQLModel
from config.db import engine


class UserBase(SQLModel):
    name: str
    email: str
    password: str


class Users(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


SQLModel.metadata.create_all(engine)
