from starlette.requests import Request

from typing import Optional

from fastapi import APIRouter
from app.models.response import NormalResponsesData

router = APIRouter(
    prefix='/admin'
)


@router.put('/account/accept', response_model=NormalResponsesData)
def put_admin_account_accept(account_id: str) -> NormalResponsesData:
    """
    accept everyone account application
    """
    pass


@router.put('/account/close', response_model=NormalResponsesData)
def put_admin_account_close(account_id: str) -> NormalResponsesData:
    """
    close everyone account
    """
    pass


@router.get('/account/pending', response_model=NormalResponsesData)
def get_admin_account_pending(
    start_page: int,
    page_size: int,
    role: Optional[str] = None,
    department: Optional[str] = None,
) -> NormalResponsesData:
    """
    get a list of user account application
    """
    pass


@router.put('/account/reject', response_model=NormalResponsesData)
def put_admin_account_reject(account_id: str) -> NormalResponsesData:
    """
    reject everyone account application
    """
    pass


@router.post('/login', response_model=NormalResponsesData)
def post_admin_login(request: Request) -> NormalResponsesData:
    """
    login admin account
    """
    pass


@router.post('/logout', response_model=NormalResponsesData)
def post_admin_logout() -> NormalResponsesData:
    """
    logout admin account
    """
    pass
