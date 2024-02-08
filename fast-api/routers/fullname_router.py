from fastapi import APIRouter
from models import User

router = APIRouter()
users = []

# Create a new user
@router.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user) 
    return user

# Get the full name of a user from their first and last names
@router.get("/user", response_model=str)
async def get_user(user: User):
    full_name = f"{user.first_name} {user.last_name}"
    return full_name