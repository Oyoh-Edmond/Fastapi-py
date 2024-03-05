from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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

my_posts = [{
    "title": "post 1", 
    "content": "content post 1",
    "id": 1},
    {
    "title": "food", 
    "content": "i love pizza",
    "id": 2
    }]

# func to retrieve a post
def find_post(id):
    for p in my_posts:
        if p["id"] == id: 
            return p
        
# func to deleting a post
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# @app.get("/")
# def greeting():
#     return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

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


# Create a post 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post): 
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}

# get recent post
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"latest": post}

# get users post with id
# convert id to integer 
# manipulate the response 
@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'message': f"post with id: {id} was not found"}
    return{"post_detail": post} 

# deleting post
# find the index in the array that has required ID
# my_posts.pop(index)
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT )

# update 

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
       
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
   
    return {'data': post_dict}  
  
   

    