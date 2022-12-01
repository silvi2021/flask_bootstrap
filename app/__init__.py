from flask import Flask
from config import Config
from app.extensions import db, migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here

    from app.memes import bp as memes_bp
    app.register_blueprint(memes_bp, url_prefix='/memes')


    # Main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # Messages blueprint
    from app.messages import bp as messages_bp
    app.register_blueprint(messages_bp, url_prefix='/messages')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app