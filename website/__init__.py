from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize Database

app_db = SQLAlchemy()
DB_NAME = "account.db"



def create_application():
    app = Flask(__name__)  #Represents the name of the file.
    app.config['SECRET_KEY'] = 'DKJSDKFJSLDKFKJDKJF'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Incorrect SQLite link which is corrected to sqlite:///{DB_NAME}

    app_db.init_app(app)
    
    from .web_design import web_design
    from .login_auth import login_auth

    app.register_blueprint(web_design, url_prefix='/')
    app.register_blueprint(login_auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):

    if not path('website/' + DB_NAME):
        app_db.create_all(app=app)
        print('Created Database!')