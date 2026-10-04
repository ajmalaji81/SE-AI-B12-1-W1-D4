import fastapi
from fastapi import FastAPI
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hi Ajmal": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q} 