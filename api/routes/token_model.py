from pydantic import BaseModel

class TokenRequestModel(BaseModel):
    grant_type: str = None
    scope: str = None
    client_id: str = None
    client_secret: str = None

class TokenResponseModel(BaseModel):
    access_token: str = None
    token_type: str = None
