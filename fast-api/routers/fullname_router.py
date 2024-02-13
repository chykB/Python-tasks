from fastapi import APIRouter
import os
from models import User

router = APIRouter()
users = []

# Create a new user
@router.post("/users/")
async def create_user(user: User):
    users.append(user) 
    return user


# Get the full name of a user from their first and last names
@router.get("/user")
async def get_user(user: User):
    full_name = f"{user.first_name} {user.last_name}"
    return full_name
