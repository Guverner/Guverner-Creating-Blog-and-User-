from typing import  Optional
from pydantic import BaseModel
from typing import List



class Blog(BaseModel):
    title : str
    body : str


class Users(BaseModel):
    name: str
    email : str
    password : str

    
class Show_User(BaseModel):
    name: str
    email: str
    blog : List[Blog]= []
    class Config():
        orm_mode = True



class Show_Blog(BaseModel):
    title: str
    body : str
    creator : Show_User
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : Optional[str] = None