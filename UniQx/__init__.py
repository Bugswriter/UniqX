from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from UniQx.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'


def create_app(class_config=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	from UniQx.main.routes import main
	from UniQx.user.routes import user
	from UniQx.profile.routes import profile
	from UniQx.post.routes import post
	app.register_blueprint(user)
	app.register_blueprint(main)
	app.register_blueprint(profile)
	app.register_blueprint(post)
	return app
