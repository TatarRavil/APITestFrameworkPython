from pydantic import BaseModel, validator, Field
from src.enums import user_enums
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: user_enums.Genders
    status: user_enums.Statuses
    date: Optional[str]

    @validator('email')
    def check_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(user_enums.UserErrors.WRONG_EMAIL.value)


class User1(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
