from __future__ import annotations

from typing import Optional

from datetime import date

from pydantic import BaseModel


class Voucher(BaseModel):
    code: str
    serial_no: str
    amount: int
    vtime: Optional[date] = None
    vtype: str
    comment: Optional[str] = None
