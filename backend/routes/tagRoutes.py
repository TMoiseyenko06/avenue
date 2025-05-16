from flask import Blueprint
from controllers import tagControllers

tag_blueprint = Blueprint('tag_blueprint',__name__)
tag_blueprint.route('/get_all_tags',methods=['GET'])(tagControllers.get_all_tags)