from typing import Annotated
from pydantic import BaseModel, model_validator, EmailStr, StringConstraints, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class RegistrationRequest(BaseModel):
    telegram_id: str
    email: EmailStr = Field(pattern=".*@student\.21-school\.ru$")

    class Config:
        json_schema_extra = {
            "example": {
                "telegram_id": "123456789",
                "email": "pintoved@student.21-school.ru",
            }
        }
