
from pydantic import BaseModel




class Blog(BaseModel):
    title: str
    body: str

# class ShowBlog(Blog):
#     class Config():
#         orm_mode = True
# we could use like this to get default block of Blog but we do as below

class ShowBlog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str