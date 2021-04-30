from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, SecretStr


class NormalResponsesData(BaseModel):
    token: Optional[str] = None
    code: int
    message: str
