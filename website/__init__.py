from flask import Flask
def create_app():
    app = Flask(__name__)
    # Load configuration
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .routes import routes
    from .auth import auth
    # Register blueprints
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 