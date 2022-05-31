from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class  Blog_posts(Base):
    __tablename__ = 'blogpost'
    
    id = Column(Integer, primary_key= True, index = True)
    title = Column (String)
    body = Column (String)
    user_id = Column (Integer, ForeignKey("users.id"))
    
    creator = relationship ("Users", back_populates = 'blogs')
    

    
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index = True)
    name = Column (String)
    email = Column (String)
    password = Column (String)


    blogs = relationship ('Blog_posts', back_populates = "creator")