from typing import Annotated
from pydantic import BaseModel, model_validator, EmailStr, StringConstraints
from pydantic_extra_types.phone_numbers import PhoneNumber


class RegistrationRequest(BaseModel):
    nickname: Annotated[
        str, StringConstraints(strip_whitespace=True,
                               min_length=1, max_length=256)
    ]
    email: EmailStr
    phone_number: PhoneNumber
    password: Annotated[
        str, StringConstraints(strip_whitespace=True,
                               min_length=7, max_length=256)
    ]

    class Config:
        json_schema_extra = {
            "example": {
                "nickname": "pintoved",
                "email": "pintoved@student.21-school.ru",
                "phone_number": "+79241325785",
                "password": "mysecretpassword"
            }
        }


class LoginRequest(BaseModel):
    email: EmailStr
    password: Annotated[
        str, StringConstraints(strip_whitespace=True,
                               min_length=7, max_length=256)
    ]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "pintoved@student.21-school.ru",
                "password": "mysecretpassword"
            }
        }


class ForgotPasswordRequest(BaseModel):
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "email": "pintoved@student.21-school.ru"
            }
        }


class ChangePasswordRequest(BaseModel):
    email: EmailStr
    old_password: Annotated[
        str, StringConstraints(strip_whitespace=True,
                               min_length=7, max_length=256)
    ]
    new_password: Annotated[
        str, StringConstraints(strip_whitespace=True,
                               min_length=7, max_length=256)
    ]

    @model_validator(mode='after')
    def check_passwords_not_match(self) -> 'ChangePasswordRequest':
        if self.old_password == self.new_password:
            raise ValueError('Passwords match')
        return self

    class Config:
        json_schema_extra = {
            "example": {
                "email": "pintoved@student.21-school.ru",
                "old_password": "mysecretpassword",
                "new_password": "mynewsecretpassword"
            }
        }
