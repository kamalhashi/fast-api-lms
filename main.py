from typing import List, Optional
from xmlrpc.client import boolean
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
)


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "Hello World"}


@app.get("/user/{id}")
async def get_user(id: int):
    return users[id]
