import hashlib
from pydantic import BaseModel, validator
from typing import Optional

class UserModel(BaseModel):
    id: Optional[int] = 0
    username: str = ''
    password: str = ''

    @validator("password", always=True)
    def set_password(cls, v, values, **kwargs):
        return hashlib.md5(v.encode('UTF-8')).hexdigest()
