from flask import Flask

def create_application():
    application = Flask(__name__)  #Represents the name of the file.
    application.config['SECRET_KEY'] = 'DKJSDKFJSLDKFKJDKJF'
    
    from .web_design import web_design
    from .login_auth import login_auth

    application.register_blueprint(web_design, url_prefix='/')
    application.register_blueprint(login_auth, url_prefix='/')

    return application
