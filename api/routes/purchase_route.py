from fastapi import APIRouter, Depends, HTTPException, Header
from .token_repository import TokenRepository
from fastapi.security import OAuth2PasswordBearer

purchase_router = APIRouter()
token_repository = TokenRepository()

def is_valid_token(token:str):
    validated = token_repository.validate_token(token)
    print('Balls', validated)
    if not token_repository.validate_token(token):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"token": "XXX"},
        )

@purchase_router.get('/purchase')
async def get_purchase(token = Header()):
    is_valid_token(token)
    return [
        {'product': 'apple', 
         'price_per_item': 1.00, 
         'quantity': 3, 
         'currency': 'ZK'}, {
         'product': 'socks', 
         'price_per_item': 22.00, 
         'quantity': 73, 
         'currency': 'ZK'
         }]
