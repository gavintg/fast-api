from fastapi import APIRouter
from .user_model import UserModel 
from .user_repository import UserRepository

user_router = APIRouter()

@user_router.post('/user')
async def create_user(user:UserModel):
    repository = UserRepository()
    return repository.insert(user)

@user_router.get('/user/{user_id}')
async def get_user(user_id:int):
    repository = UserRepository()
    return repository.select_by_id(user_id)
