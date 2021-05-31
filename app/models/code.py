from __future__ import annotations


from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .voucher import Voucher  # noqa: F401


class Code(Base):
    __tablename__ = 't_juju_code'
    code = Column(String(100), index=True, nullable=False, unique=True)
    vtype = Column(String(50), nullable=False)
    comment = Column(String(150), nullable=True)

    voucher = relationship("Voucher", back_ref="t_juju_code")
