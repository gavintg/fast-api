from pydantic import BaseModel, validator
from typing import Optional
from .common.password_hash import PasswordHash

class UserModel(BaseModel):
    id: Optional[int] = 0
    username: str = ''
    password: str = ''

    @validator("password", always=True)
    def set_password(cls, v, values, **kwargs):
        return PasswordHash().get_hashed_password(v.encode('UTF-8'))
