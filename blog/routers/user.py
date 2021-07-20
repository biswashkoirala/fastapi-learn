from blog import database
from blog.database import get_db
from fastapi import APIRouter, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

get_db= database.get_db





@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(get_db)):    
    return user.create(request,db)

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)