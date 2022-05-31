from fastapi import APIRouter, Depends, Response, HTTPException,status
import schemas, models
from sqlalchemy.orm import Session
from database import  SessionLocal, get_db



router = APIRouter()




@router.get('/return-all-blogs', tags= ['Blog'])
def return_all_blogs(db:Session = Depends(get_db)):
    return db.query(models.Blog_posts).all()
    



# Creating Blog
@router.post('/blog-create-blog',status_code=status.HTTP_201_CREATED, tags= ['Blog'])
def create_blog(request : schemas.Blog, db:Session= Depends(get_db)):
    new_blog = models.Blog_posts(title= request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Retun all Blogs
@router.get('/return-all-blogs', tags= ['Blog'])
def return_all_blogs(db:Session = Depends(get_db)):
    return db.query(models.Blog_posts).all()

# Updating Blog 

@router.put('/blog-update-user{id}', status_code=status.HTTP_202_ACCEPTED,  tags= ['Blog'])
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    db.query(models.Blog_posts).filter(models.Blog_posts.id==id).update(request)
    db.commit()
    return 'updated'
    
   
#Show only title and body of blog, without id.

@router.get('/return-title-blog/{id}', response_model=schemas.Show_Blog, tags= ['Blog'])
def show_title_body(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog_posts).filter(models.Blog_posts.id==id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail= f'Blog with {id}, ID is not found'
        )
    
    return blog

# Deleting blog with ID

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags= ['Blog'])
def delete_blog(id, db:Session = Depends(get_db)):
    delete_blog = db.query(models.Blog_posts).filter(models.Blog_posts.id==id).delete(synchronize_session=False)
    if not delete_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail= f'Blog post with {id}, not found'
        )
    return db.query(models.Blog_posts).all(), db.commit(), 
    