from sqlalchemy.orm import Session
from..models.account import Account
from..schemas.account import AccountCreate, AccountUpdate, AccountResponse

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account: AccountCreate):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def update_account(db: Session, account_id: int, account: AccountUpdate):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        return None
    for key, value in account.dict(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db: Session, account_id: int):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        return None
    db.delete(db_account)
    db.commit()
    return db_account