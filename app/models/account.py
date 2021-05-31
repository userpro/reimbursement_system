from __future__ import annotations


from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .voucher import Voucher  # noqa: F401


class Account(Base):
    __tablename__ = 't_juju_account'
    name = Column(String(10), index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(20), nullable=False)
    department = Column(String(100), nullable=True)
    role = Column(Integer, nullable=False)  # 0: normal, 1: subadmin, 2: admin
    enable = Column(Integer, nullable=False)  # 0: disable, 1: able
    ip = Column(String(150), nullable=True)

    voucher = relationship("Voucher", back_ref="t_juju_account")
