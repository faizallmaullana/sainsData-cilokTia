from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from app.urls import __URLPATH__
    __URLPATH__()
    api.init_app(app)
    
    from app.models.pedagang import Data_pedagang
    Migrate(app, db)

    return app