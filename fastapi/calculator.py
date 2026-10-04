from fastapi import FastAPI
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

app = FastAPI(
    title="Calculator API",
    description="A simple calculator API using FastAPI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Calculator API",
        "docs": "/docs"
    }


@app.get("/add")
def add(a: float, b: float):
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": a + b
    }


@app.get("/subtract")
def subtract(a: float, b: float):
    return {
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": a - b
    }


@app.get("/multiply")
def multiply(a: float, b: float):
    return {
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": a * b
    }


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {
            "error": "Cannot divide by zero"
        }

    return {
        "operation": "division",
        "a": a,
        "b": b,
        "result": a / b
    }