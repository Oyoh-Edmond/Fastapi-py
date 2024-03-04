from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel, Field, Json
from  random import randrange

app = FastAPI()


# create a Schema to restrict user input
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None 
    id: int

my_posts = [{
    "title": "post 1", 
    "content": "content post 1",
    "id": 1},
    {
    "title": "food", 
    "content": "i love pizza",
    "id": 2
    }]

# to retrieve a post
def find_post(id):
    for p in my_posts:
        if p["id"] == id: 
            return p

# @app.get("/")
# def greeting():
#     return {"message": "Hello World"}

# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}

# @app.post("/posts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# @app.post("/posts")
# def create_posts(new_posts: Post):
#     print(new_posts.rating)
#     return {"data":"new post"}


# @app.post("/posts")
# def get_post():
#     return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post): 
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}


# get users post with id
#convert id to integer 

@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(id)
    return{"post_detail": post} 




