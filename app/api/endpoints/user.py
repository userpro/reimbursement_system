from starlette.requests import Request

from fastapi import APIRouter
from app.schemas.response import NormalResponsesData
from app.schemas.voucher import Voucher

router = APIRouter(
    prefix='/user'
)


@router.post('/login', response_model=NormalResponsesData)
def post_user_login(request: Request) -> NormalResponsesData:
    """
    login user account
    """
    pass


@router.post('/logout', response_model=NormalResponsesData)
def post_user_logout() -> NormalResponsesData:
    """
    logout user account
    """
    pass


@router.post('/register', response_model=NormalResponsesData)
def post_user_register(request: Request) -> NormalResponsesData:
    """
    register new user account
    """
    pass


@router.get('/voucher', response_model=NormalResponsesData)
def get_user_voucher(start_page: int, page_size: int) -> NormalResponsesData:
    """
    get a list of voucher
    """
    pass


@router.put('/voucher', response_model=NormalResponsesData)
def put_user_voucher(body: Voucher) -> NormalResponsesData:
    """
    modify voucher info
    """
    pass


@router.post('/voucher', response_model=NormalResponsesData)
def post_user_voucher(body: Voucher) -> NormalResponsesData:
    """
    add new voucher
    """
    pass
