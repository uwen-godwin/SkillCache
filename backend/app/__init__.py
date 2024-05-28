from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from .routes import portfolio, skills, projects
        app.register_blueprint(portfolio.bp)
        app.register_blueprint(skills.bp)
        app.register_blueprint(projects.bp)
        
        return app
