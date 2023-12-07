from datetime import datetime
from pydantic import BaseModel
from typing import List


class CustomerId(BaseModel):
    id: int


class CustomerName(BaseModel):
    name: str


class BranchIds(BaseModel):
    branch_ids: int


class IsStudy(BaseModel):
    is_study: bool


class LegalType(BaseModel):
    legal_type: bool


class DateFrom(BaseModel):
    date_from: datetime


class DateTo(BaseModel):
    date_to: datetime


class Phone(BaseModel):
    phone: str
