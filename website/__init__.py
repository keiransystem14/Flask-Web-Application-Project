from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize Database

app_db = SQLAlchemy()
DB_NAME = "account.db"



def create_application():
    application = Flask(__name__)  #Represents the name of the file.
    application.config['SECRET_KEY'] = 'DKJSDKFJSLDKFKJDKJF'
    application.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite://{DB_NAME}' #RuntimeError: Entered incorrect syntax - 'SQLAlchemy_DATABASE_URI'. Changed to 'SQLALCHEMY_DATABASE_URI'

    app_db.init_app(application)
    
    from .web_design import web_design
    from .login_auth import login_auth

    application.register_blueprint(web_design, url_prefix='/')
    application.register_blueprint(login_auth, url_prefix='/')

    from . import User, Note 

    create_database(application)

    return application

def create_database(application):

    if not path('website/' + DB_NAME):
        app_db.create_all(application=application)
        print('Created Database!')