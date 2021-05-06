from __future__ import annotations


from typing import TYPE_CHECKING


from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .account import Account  # noqa: F401
    from .code import Code  # noqa: F401


class Voucher(Base):
    __tablename__ = 'voucher'
    code = Column(String(100), index=True)
    serial_no = Column(String(120), index=True)
    amount = Column(Integer, default=0, nullable=False)
    vtime = Column(DateTime(timezone=True), nullable=False)

    vtype = Column(String(50), ForeignKey("code.id"))

    comment = Column(String(150), nullable=True)
    create_time = Column(DateTime(timezone=True), default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())

    uid = Column(Integer, ForeignKey("account.id"))
