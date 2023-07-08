from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=3)
    title: str

    # @validator('id')
    # def check(cls, v):
    #     if v > 2:
    #         raise ValueError('id is not valid')
    #     else:
    #         return v
