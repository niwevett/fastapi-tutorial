from datetime import date
from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import asc, null
from sqlalchemy import func

from app import oauth2

from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, creation_since: date = "1999.01.01", skip: int = 0, search: Optional[str] = ""):
    # crusor.excecute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    #if private mode
        #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).order_by(asc(models.Post.id)).all()
    
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).order_by(asc(models.Post.id)).limit(limit).offset(skip)
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()

    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cursor.fetchone()
    #post = db.query(models.Post).filter(models.Post.id == id).first()
 
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail = f"Post with id: {id} was not found")
    return post

@router.put("/{id}", response_model=schemas.Post)
def update_posts(id: int, update_post: schemas.PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""UPDATE  posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #            (post.title, post.content, post.published, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with the id: {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to update this post")

    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE from posts WHERE id = %s RETURNING * """, (str(id),))
    #post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()


    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Deleting not possible. Post with the id: {id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to update this post")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)