from typing import List, Optional

import secrets
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: Optional[str]
    SERVER_HOST: Optional[AnyHttpUrl]

    PROJECT_NAME: str = 'juju reimbursement system'
    PROJECT_VERSION: str = '1.0'

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:8080']

    SQLALCHEMY_DATABASE_URI = ''


settings = Settings()
