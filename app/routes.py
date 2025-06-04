from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Schema for user registration
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserRegister):
    return {"message": "User registered successfully", "user": user}

@router.get("/hello")
async def say_hello():
    return {"message": "Hello from the routes!"}


