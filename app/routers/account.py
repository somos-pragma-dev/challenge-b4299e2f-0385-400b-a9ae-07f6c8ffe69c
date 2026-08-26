from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..core.config import SessionLocal
from..dependencies.security import get_current_user
from..services.account_service import get_account_by_id, create_account, update_account, delete_account
from..schemas.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/accounts/', response_model=AccountResponse)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    return create_account(db, account)

@router.get('/accounts/{account_id}', response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = get_account_by_id(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@router.put('/accounts/{account_id}', response_model=AccountResponse)
def update_account_endpoint(account_id: int, account: AccountUpdate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = update_account(db, account_id, account)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@router.delete('/accounts/{account_id}', response_model=AccountResponse)
def delete_account_endpoint(account_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    db_account = delete_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account