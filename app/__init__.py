from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
simple = SimpleMDE()


auth = Blueprint('auth',__name__)

# from . import views

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    # Will add the views and forms

    # setting config
    # from .requests import configure_request
    # configure_request(app)

    # configure UploadSet
    configure_uploads(app,photos)
    
# git 
    return app