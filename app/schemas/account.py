from typing import Optional

from pydantic import BaseModel, EmailStr, IPvAnyNetwork


# Shared properties
class AccountBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    department: str
    # role: int = 0 # can't send from the API
    enable: int = 0
    password: Optional[str] = None
    ip: Optional[IPvAnyNetwork] = None


# Properties to receive via API on creation
class AccountCreate(AccountBase):
    pass


# Properties to receive via API on update
class AccountUpdate(AccountBase):
    pass


class AccountInDBBase(AccountBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    pass
