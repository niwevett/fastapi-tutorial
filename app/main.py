from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .confiq import settings
from fastapi.middleware.cors import CORSMiddleware

#tämä käytössä jos ei käytä alembic
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, prefix="/posts", tags=['Posts'])
app.include_router(user.router, prefix="/users", tags=['Users'])
app.include_router(vote.router, prefix="/vote", tags=['Votes'])
app.include_router(auth.router, tags=['Authentication'])

@app.get("/")
def root():
    return {"message": "Welcome to my API!!"}