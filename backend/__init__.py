from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models here to register them with SQLAlchemy
    from backend.models import User, Portfolio, Skill, Project
    
    # Register blueprints
    from backend.routes import portfolio, skills, projects
    app.register_blueprint(portfolio.bp)
    app.register_blueprint(skills.bp)
    app.register_blueprint(projects.bp)

    return myapp
