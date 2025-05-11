from utils.util import requires_auth
from sqlalchemy.orm import Session
from database import db
from  models.userModels import User
from flask import request, jsonify
import requests
from dotenv import load_dotenv
import os
from models.tagModels import Tag

load_dotenv()
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
AUTH0_CLIENT = os.getenv('AUTH0_CLIENT')
AUTH0_SECRET = os.getenv('AUTH0_SECRET')




@requires_auth
def check_user(subject):
    with Session(db.engine) as session:
        with session.begin():
            user = session.query(User).filter_by(subject = subject).first()
            return True if user else False

@requires_auth
def create_new_user(subject):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(
                subject=subject,
                tags=[]
            )
            session.add(new_user)
            session.commit()
            return jsonify({"status":"OK"}), 201



def get_existing_user():
    pass

@requires_auth
def update_user_profile(subject,user_data):
    with Session(db.engine) as session:
        with session.begin():
            user = session.query(User).filter_by(subject=subject).first()
            if 'email' in user_data:
                user.email = user_data['email']
            if 'phone' in user_data:
                user.phone = user_data['phone']
            if 'tags' in user_data:
                tags = session.query(Tag).filter(Tag.id.in_(user_data['tags'])).all()

