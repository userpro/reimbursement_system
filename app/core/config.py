from typing import AnyHttpUrl
import secrets
from pydantic import BaseSettings


class Settings(BasicSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl

    PROJECT_NAME: str = 'juju reimbursement system'
    PROJECT_VERSION: str = '1.0'

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:8080']


settings = Settings()
