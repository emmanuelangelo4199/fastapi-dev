from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def read_item():
    return {"posts":"This is my post"}

@app.post("/createPost")
def create_post(new_post: Post):

    print(new_post)
    return {"data ": "new post"}