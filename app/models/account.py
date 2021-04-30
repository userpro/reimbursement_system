from __future__ import annotations

from datetime import date

from pydantic import BaseModel, SecretStr


class Account(BaseModel):
    name: str
    password: SecretStr
