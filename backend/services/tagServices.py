from utils.util import requires_auth
from sqlalchemy.orm import Session
from database import db
from  models.userModels import User
from flask import request, jsonify
import requests
from dotenv import load_dotenv
import os
from models.tagModels import Tag
from schema import TagSchema
from pydantic import TypeAdapter



@requires_auth
def get_user_tags(subject):
    with Session(db.engine) as session:
        with session.begin():
            user = session.query(User).filter_by(subject=subject).first()
            adapter = TypeAdapter(list[TagSchema])
            tag_schemas = adapter.validate_python(user.tags)
            return jsonify(tag_schemas)
        
def get_all_tags():
    with Session(db.engine) as session:
        with session.begin:
            tags = session.query(Tag).all()
            adapter = TypeAdapter(list[TagSchema])
            tag_schemas

            