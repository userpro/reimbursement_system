from typing import Optional

from pydantic import BaseModel


# Shared properties
class VoucherBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class VoucherCreate(VoucherBase):
    title: str


# Properties to receive on item update
class VoucherUpdate(VoucherBase):
    pass


# Properties shared by models stored in DB
class VoucherInDBBase(VoucherBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Voucher(VoucherInDBBase):
    pass


# Properties properties stored in DB
class VoucherInDB(VoucherInDBBase):
    pass
