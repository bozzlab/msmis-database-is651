from datetime import date

from fastapi import HTTPException, status


from pydantic import BaseModel, validator, Field, conint, EmailStr
from app.constants.gender_type import GenderType
from app.constants.user_status_type import UserStatusType


class Reference(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ReferenceLevel(Reference):
    level: str


class Occupation(Reference):
    pass


class WorkExperienceLevel(ReferenceLevel):
    pass


class EducationLevel(ReferenceLevel):
    pass


class Currency(Reference):
    code: str
    name: str | None


class PostalCode(Reference):
    postal_code: str


class UserBase(BaseModel):
    username: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=50)
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    email: EmailStr | str
    dob: date
    gender: GenderType
    occupation_id: conint(ge=1)
    work_experience_level_id: conint(ge=1)
    education_level_id: conint(ge=1)
    postal_code_id: conint(ge=1)
    currency_id: conint(ge=1)
    personal_data_consent: bool
    marketing_consent: bool


class UserCreate(UserBase):
    password_hash: str = Field(..., max_length=255)

    @validator("dob")
    def validate_age(cls, v):
        today = date.today()
        age = today.year - v.year - ((today.month, today.day) < (v.month, v.day))

        if age < 18:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to create user because under 18 years old",
            )

        return v


class UserLogin(BaseModel):
    username: str = Field(..., max_length=255)
    password_hash: str = Field(..., max_length=255)


class UserUpdate(UserBase):
    first_name: str = Field(None, max_length=100)
    last_name: str = Field(None, max_length=100)


class UserStatus(BaseModel):
    status: UserStatusType


class UserResponse(UserBase):
    status: str
    id: int

    occupation: Occupation
    work_experience_level: WorkExperienceLevel
    education_level: EducationLevel
    postal_code: PostalCode
    currency: Currency

    class Config:
        orm_mode = True
