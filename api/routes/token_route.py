from fastapi import APIRouter, Response
from .token_model import TokenRequestModel, TokenResponseModel
from .user_repository import UserRepository
from .common.password_hash import PasswordHash

token_router = APIRouter()

repository = UserRepository()
password = PasswordHash()

def authorised_200(response: Response) -> TokenResponseModel:
    response.status_code = 200
    return TokenResponseModel(access_token=None, token_type='Bearer')

def unauthorised_401(response: Response) -> TokenResponseModel:
    response.status_code = 401
    return TokenResponseModel(access_token=None, token_type=None)

@token_router.post('/token')
async def token_request(token_request:TokenRequestModel, response: Response):
    user = repository.select_by_username(token_request.client_id)
    if user == None: 
        return unauthorised_401(response)
    auth_result = password.check_hashed_password(token_request.client_secret, user.hashed_password)
    if auth_result == True:
        return authorised_200(response)
    return unauthorised_401(response)
