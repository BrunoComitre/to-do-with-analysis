import string
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, Union
from bson.objectid import ObjectId


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr

# TO-DO : ACRESCENTAR SE O USUÁRIO ESTÁ OU NÃO ATIVO

class UserCreateSchema(UserBaseSchema):
    password: str = Field(min_length=8)

    @validator('password')
    def check_password(cls, v):
        if cls.check_password_complexity(v):
            return v
        else:
            raise ValueError("The password doesn't match the complexity criteria")
    
    @staticmethod
    def check_password_complexity(passwd: str):
        lowercase = any([True if item in string.ascii_lowercase else False for item in passwd])
        uppercase = any([True if item in string.ascii_uppercase else False for item in passwd])
        digits = any([True if item in string.digits else False for item in passwd])
        return all([lowercase, uppercase, digits])

class UserUpdateSchema(UserBaseSchema):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

class UserInDb(UserBaseSchema):
    id : str = Field(alias="_id")

    @validator('id', pre=True)
    def convert_object_id_to_str(cls, v):
        return str(v)

    class Config:
        orm_mode = True

class UserSchema(UserInDb):
    pass
