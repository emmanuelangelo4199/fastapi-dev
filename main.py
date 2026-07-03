from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None


my_posts = [
            {"title": "post of posts 1", "content": "content of posts 1", "id": 1},
            
            {"title":"title of titles", "content":"contents of contents", "id":3},

            {"title":"title of titles 2", "content":"contents of contents 2", "id":2},
            
            ]

# not the best way!!!!
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def read_item():
    return {"data":my_posts}

@app.post("/posts")
def create_post(post: Post):

    post_dict = post.model_dump()
    # model_dump()  also the same as dict()
    post_dict ['id'] = randrange(0, 1000000)

    my_posts.append(post_dict)
    return {"data ": post_dict}

@app.get ("/posts/{id}")
def get_post(id):
    # converting the id to an integer to avoid a null output
    post = find_post(int(id))
    return {"get_post": post}