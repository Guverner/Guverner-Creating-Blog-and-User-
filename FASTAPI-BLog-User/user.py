#Create User
from fastapi import APIRouter, Depends, Response, HTTPException,status
import schemas, models
from sqlalchemy.orm import Session
from database import  SessionLocal, get_db
from hashing import Hash

router = APIRouter()


@router.post ('/user-create-user', status_code=status.HTTP_201_CREATED, tags= ['User'])
def create_user(request: schemas.Users, db:Session = Depends(get_db)):
    
    new_user = models.Users(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Show all Users

@router.get('/show-all-users', status_code=status.HTTP_200_OK, tags=['User'])
def show_all_users(db:Session = Depends (get_db)):
    return db.query(models.Users).all()

# Show user by ID

@router.get('/users-retun-user/{id}', response_model= schemas.Show_User, tags= ['User'])
def get_user(id : int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id== id). first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'User with id {id} not found'
        )
    return user



# Delete User and retun other users
@router.delete('/delete-user/{id}',status_code= status.HTTP_301_MOVED_PERMANENTLY, tags=['User'] )
def delete_user(id, db: Session = Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.id==id).delete(synchronize_session=False)
    if not user :
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,
        detail= f'User with {id} is not found'           
        )
    return db.query(models.Users).all(),db.commit()