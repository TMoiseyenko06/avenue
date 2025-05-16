from utils.util import requires_auth
from sqlalchemy.orm import Session
from database import db
from  models.userModels import User
from flask import request, jsonify
import requests
from dotenv import load_dotenv
import os
from models.tagModels import Tag
from middleware.tagSchema import tags_schmea



@requires_auth
def get_user_tags(subject):
    with Session(db.engine) as session:
        with session.begin():
            user = session.query(User).filter_by(subject=subject).first()
            tags = user.tags
            return tags_schmea.jsonify(tags)
        
def get_all_tags():
    with Session(db.engine) as session:
        with session.begin():
            tags = session.query(Tag).all()
            return tags_schmea.jsonify(tags)
            

