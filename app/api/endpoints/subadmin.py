from starlette.requests import Request

from typing import Any

from fastapi import APIRouter
from app.schemas.response import NormalResponsesData

router = APIRouter(
    prefix='/subadmin'
)


@router.put('/account/accept', response_model=NormalResponsesData)
def put_subadmin_account_accept(account_id: str) -> NormalResponsesData:
    """
    accept a user account application belonging to this department
    """
    pass


@router.put('/account/close', response_model=NormalResponsesData)
def put_subadmin_account_close(account_id: str) -> NormalResponsesData:
    """
    close a user account belonging to this department
    """
    pass


@router.get('/account/pending', response_model=NormalResponsesData)
def get_subadmin_account_pending(
    start_page: int, page_size: int
) -> NormalResponsesData:
    """
    get a list of account application belonging to this department
    """
    pass


@router.put('/account/reject', response_model=NormalResponsesData)
def put_subadmin_account_reject(account_id: str) -> NormalResponsesData:
    """
    reject a user account application belonging to this department
    """
    pass


@router.post('/register', response_model=NormalResponsesData)
def post_subadmin_register(body: Any) -> NormalResponsesData:
    """
    register subadmin account
    """
    pass


@router.put('/voucher/accept', response_model=NormalResponsesData)
def put_subadmin_voucher_accept(voucher_id: str) -> NormalResponsesData:
    """
    accept a voucher application belonging to this department
    """
    pass


@router.put('/voucher/reject', response_model=NormalResponsesData)
def put_subadmin_voucher_reject(voucher_id: str) -> NormalResponsesData:
    """
    reject a voucher application belonging to this department
    """
    pass
