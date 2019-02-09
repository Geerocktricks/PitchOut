from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

auth = Blueprint('auth',__name__)

# from . import views

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Will add the views and forms

    # setting config
    # from .requests import configure_request
    # configure_request(app)
# git 
    return app