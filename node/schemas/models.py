from pydantic import BaseModel

class Email(BaseModel):
    email: str

class Datetime(BaseModel):
    datetime: str
