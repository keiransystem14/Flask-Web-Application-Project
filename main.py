from website import create_application

application = create_application()

if __name__ == '__main__':
    application.run(debug=True) # If any changes were made to python code, it will automatically re-run the server. This is for staging.