from services.userServices import *
from flask import jsonify

def create_user():
    user_exists = check_user()
    if user_exists:
        return jsonify({"error":"user already exists"}), 400
    return create_new_user()