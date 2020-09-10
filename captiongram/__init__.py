from flask import Flask
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from captiongram.config import Config
#db
db = SQLAlchemy()
bcrypt = Bcrypt()

#init login mannager
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #db init 
    db.init_app(app)
     
    #user part 
    from captiongram.users.routes import users
    app.register_blueprint(users)


    #login handler 
    bcrypt.init_app(app)
    login_manager.init_app(app)
   

    return app

