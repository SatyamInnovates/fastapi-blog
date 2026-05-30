from fastapi import APIRouter,Depends,status,HTTPException
from  .. import schemas,database,models,oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
from blog.repository import blog as blog_repository

router = APIRouter(prefix="/blog",tags=['blogs'])
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),
           current_user = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user.id)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)
    
    
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)    
def update(id,request:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)


@router.get('/{id}', response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db),
         current_user = Depends(oauth2.get_current_user)):
    return blog_repository.show(id, db)
