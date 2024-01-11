from fastapi import FastAPI
from apis import api_router
from dao.engine_factory import EngineFactory

app = FastAPI()
app.include_router(api_router.router)


@app.get("/")
async def root():
    EngineFactory.get_engine()
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
