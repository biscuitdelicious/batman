from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

load_dotenv()
# Get your FIREBASE_KEY from https://console.firebase.google.com/u/0/project/bytelearning-1e3b6/settings/serviceaccounts/adminsdk
FIREBASE_API_KEY = os.getenv('FIREBASE_KEY')

cred = credentials.Certificate(FIREBASE_API_KEY)
default_app = firebase_admin.initialize_app(cred)

app = FastAPI(title='ByteLearning')

@app.get('/')
async def root():
    return {'message': 'ByteLearning'}

class Problem(BaseModel):
    id: int
    name: str
    description: str
    difficulty: int
    acceptance_rate: float

class Discussion(BaseModel):
    id: int
    problem_id: int
    parent_id: int
    text: str
    date: str
    up_votes: int
    username: Optional[str] = None