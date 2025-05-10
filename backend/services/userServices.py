from utils.util import requires_auth
from sqlalchemy.orm import Session
from database import db
from  models.userModels import User
from flask import request, jsonify

@requires_auth
def check_user(payload):  
    user_subject = payload['sub']
    with Session(db.engine) as session:
        with session.begin():
            user = session.query(User).filter_by(subject = user_subject).first()
            return True if user else False

@requires_auth
def create_new_user(payload):
    user_data = request.json()
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(
                subject_id = payload['sub'],
                email = user_data['email'],
                phone = user_data['phone'] or "",
                tags = user_data['tags'] or []
            )
            session.add(new_user)
            session.commit()
            return jsonify({"status":"OK"}), 201

def get_existing_user():
    pass