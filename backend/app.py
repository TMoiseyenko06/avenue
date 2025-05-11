from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from database import db
from dotenv import load_dotenv
import os
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
    CORS(app)
    db.init_app(app)
    blue_print_config(app)
    with app.app_context():
        db.create_all()
    return app

def blue_print_config(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")

app = create_app('DevelopmentConfig')

app.run(debug=True)

