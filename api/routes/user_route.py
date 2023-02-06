from fastapi import APIRouter
from .user_model import UserModel 
from .user_repository import UserRepository

user_router = APIRouter()

@user_router.post('/user')
async def create_user(user:UserModel):
    repository = UserRepository()
    return {'user_id': repository.insert(user)}

@user_router.get('/user/{username}')
async def get_user(username:str):
    repository = UserRepository()
    return repository.select_by_username(username)
