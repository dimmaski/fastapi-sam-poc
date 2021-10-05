
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def func1():
    return {"Hello": "/"}

@app.get("/ping")
def func2():
    return {"Hello": "/ping"}

@app.get("/ping/ping")
def func3():
    return {"Hello": "/ping/ping"}

handler = Mangum(app)
