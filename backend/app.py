from flask import Flask, request, jsonify
from flask_caching import Cache
from flask_cors import CORS
from database import db
from dotenv import load_dotenv
import os
from utils.util import requires_auth
from models.eventModels import *
from models.tagModels import *
from models.userModels import *
from routes.userRoutes import user_blueprint

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def create_app(config_name):
    app = Flask(__name__)
    cache = Cache().init_app(app)
    app.config.from_object(f'config.{config_name}')
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
    db.init_app(app)
    blue_print_config(app)
    with app.app_context():
        db.create_all()
    return app

def blue_print_config(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")

app = create_app('DevelopmentConfig')

app.run(debug=True)

