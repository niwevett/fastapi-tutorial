from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import EmailStr
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

    class Config:
        orm_mode = True

class UserUpdate(UserCreate):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner:UserResponse

    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

