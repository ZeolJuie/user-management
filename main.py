from typing import Annotated, Union

from fastapi import FastAPI, Depends
from apis import api_router
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


app = FastAPI()
app.include_router(api_router.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
