from __future__ import annotations


from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import Column, ForeignKey, String, DateTime, Float, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .account import Account  # noqa: F401
    from .code import Code  # noqa: F401


class Voucher(Base):
    __tablename__ = 't_juju_voucher'
    code = Column(String(100), index=True, unique=True)
    serial_no = Column(String(120), index=True, unique=True)
    amount = Column(Float, default=0, nullable=False)
    vtime = Column(DateTime(), nullable=False)

    vtype = Column(String(50), ForeignKey("t_juju_code.vtype"))

    comment = Column(String(150), nullable=True)
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now,
                         onupdate=datetime.now)

    owner_id = Column(Integer, ForeignKey("t_juju_account.id"))
    modifier_id = Column(Integer, ForeignKey("t_juju_account.id"))
