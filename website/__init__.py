from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Database

app_db = SQLAlchemy()
DB_NAME = "account.db"



def create_application():
    application = Flask(__name__)  #Represents the name of the file.
    application.config['SECRET_KEY'] = 'DKJSDKFJSLDKFKJDKJF'
    application.config['SQLAlchemy_DATABASE_URI'] = f'sqlite://{DB_NAME}'

    app_db.init_app(application)
    
    from .web_design import web_design
    from .login_auth import login_auth

    application.register_blueprint(web_design, url_prefix='/')
    application.register_blueprint(login_auth, url_prefix='/')

    return application
