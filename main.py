from fastapi import FastAPI
from.routers import account

app = FastAPI()

app.include_router(account.router)

@app.get('/')
def read_root():
    return {'message': 'Hello World'}