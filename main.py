from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
FILE_PATH = "users.json"


class User(BaseModel):
    Username: str
    Email: str
    Password: str


def read_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def write_users(user):
    with open(FILE_PATH, "w") as f:
        json.dump(user, f, indent=2)


@app.get("/users")
def get_users():
    users = read_users()
    return users


@app.post("/users")
def create_user(user: User):
    users = read_users()
    users.append(user.model_dump())
    write_users(users)
    return {"message": "User added successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
