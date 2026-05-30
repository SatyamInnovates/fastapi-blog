from .. import schemas

from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from fastapi import HTTPException,status
from passlib.context import CryptContext
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    print("Password:", request.password)
    print("Length:", len(request.password))
    hashedPassword = Hash.bcrypt(request.password)

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashedPassword
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get(user_id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user {user_id}not registered yet")
    return user