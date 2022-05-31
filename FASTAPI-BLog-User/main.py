from fastapi import FastAPI, Depends, status, Response, HTTPException
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import blog, user, logingin

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(logingin.router)


