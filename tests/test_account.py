from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from..core.config import Config, Base
from..models.account import Account
from..schemas.account import AccountCreate
from..services.account_service import create_account

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

def test_create_account():
    db = TestingSessionLocal()
    account = AccountCreate(account_number='1234567890', balance=100.0, owner='John Doe')
    new_account = create_account(db, account)
    assert new_account.account_number == account.account_number
    assert new_account.balance == account.balance
    assert new_account.owner == account.owner