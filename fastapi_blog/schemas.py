from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str = Field(min_length=1, max_length=50, description="The username of the user")
    email: EmailStr = Field(max_length=120, description="The email address of the user")

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=200, description="The password of the user")

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    image_file: str | None
    image_path: str

class UserPrivate(UserPublic):
    email: EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50, description="The username of the user")
    email: EmailStr | None = Field(default=None, max_length=120, description="The email address of the user")
    image_file: str | None = Field(default=None, min_length=1, max_length=200,description="The image file name of the user")

class Token(BaseModel):
    access_token: str
    token_type: str
    
class PostBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(min_length=1, max_length=100, description="The title of the post")
    content: str = Field(min_length=1,description="The content of the post")
    

class PostCreate(PostBase):
    user_id:int

class PostUpdate(BaseModel):
    
    title: str | None = Field(default=None, min_length=1, max_length=100, description="The title of the post")
    content: str | None = Field(default=None, min_length=1, description="The content of the post")

class PostResponse(PostBase):
    
    id:int
    user_id:int
    likes:int
    date_posted:datetime
    author: UserPublic
    