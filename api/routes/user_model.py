import argon2
from pydantic import BaseModel, validator
from typing import Optional

class UserModel(BaseModel):
    id: Optional[int] = 0
    username: str = ''
    password: str = ''

    @validator("password", always=True)
    def set_password(cls, v, values, **kwargs):
        return argon2.hash_password(v.encode('UTF-8'))
