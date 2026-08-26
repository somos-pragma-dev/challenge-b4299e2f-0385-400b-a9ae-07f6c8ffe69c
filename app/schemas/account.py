from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    account_number: str
    balance: float
    owner: str

class AccountCreate(AccountBase):
    pass

class AccountUpdate(AccountBase):
    balance: Optional[float] = None
    owner: Optional[str] = None

class AccountResponse(AccountBase):
    id: int

    class Config:
        orm_mode = True