from flask import Blueprint
from controllers import userControllers

user_blueprint = Blueprint('user_blueprint',__name__)
user_blueprint.route('/create_user',methods=['POST'])(userControllers.create_user)