from flask import Flask
from flask_bootstrap import Bootstrap
from app.models import User
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

# Initializing application

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
