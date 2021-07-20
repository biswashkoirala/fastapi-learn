from blog.routers import authentication
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from blog import  models
from blog.database import engine
from blog.routers import blog, user, authentication, homepage


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(homepage.router)



