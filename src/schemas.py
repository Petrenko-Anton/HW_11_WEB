from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    phone: PhoneNumber
    email: Optional[EmailStr]
    birthday: Optional[datetime]
    description: Optional[str] = Field(max_length=250)


class ContactResponse(ContactModel):
    id: int

