from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, Field
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None


my_posts = [
    {"title": "post of posts 1", "content": "content of posts 1", "id": 1},
    {"title": "title of titles 2", "content": "contents of contents 2", "id": 2},
    {"title": "title of titles", "content": "contents of contents", "id": 3},
    {"title": "cast of the old war", "content": "begotten souls, devahoured by cats", "id": 4}
]

# not the best way!!!!
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def read_item():
    return {"data":my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):

    post_dict = post.model_dump()
    # model_dump()  also the same as dict()
    post_dict ['id'] = randrange(0, 1000000)

    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get ("/posts/{id}")
def get_post(id: int, response: Response):
    # converting the id to an integer to avoid a null output
    # print(type(id))
    post = find_post(id)

    if not post:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found.")
        
        # not a good way for passing http status response
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'E-message': f"post with id: {id} was not found."}

    return {"post_details": post}