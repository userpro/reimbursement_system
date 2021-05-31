import datetime

from typing import Optional

from pydantic import BaseModel


# Shared properties
class VoucherBase(BaseModel):
    code: str
    serial_no: str
    amount: float
    vtime: datetime.datetime
    vtype: str
    comment: Optional[str] = None


# Properties to receive on item creation
class VoucherCreate(VoucherBase):
    pass


# Properties to receive on item update
class VoucherUpdate(VoucherBase):
    pass


# Properties shared by models stored in DB
class VoucherInDBBase(VoucherBase):

    class Config:
        orm_mode = True


# Properties to return to client
class Voucher(VoucherInDBBase):
    pass


# Properties properties stored in DB
class VoucherInDB(VoucherInDBBase):
    owner_id: int
