from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class AccountBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class AccountCreate(AccountBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class AccountUpdate(AccountBase):
    password: Optional[str] = None


class AccountInDBBase(AccountBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    hashed_password: str
