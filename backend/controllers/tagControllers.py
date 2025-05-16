from services.tagServices import *
from flask import jsonify

def get_tags():
    return get_all_tags()