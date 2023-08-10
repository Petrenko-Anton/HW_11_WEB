from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    phone: PhoneNumber | None
    email: Optional[EmailStr]
    birthday: Optional[datetime]
    description: Optional[str] = Field(max_length=500)


class ContactResponse(ContactModel):
    id: int

class ContactUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[PhoneNumber] = None
    email: Optional[EmailStr] = None
    birthday: Optional[datetime] = None
    description: Optional[str] = None

    class Config:
        validate_assignment = True