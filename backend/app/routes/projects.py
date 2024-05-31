from flask import Blueprint, jsonify

bp = Blueprint('projects', __name__, url_prefix='/api/projects')

@bp.route('/', methods=['GET'])
def get_projects():
    # This is just a placeholder. You would fetch from the database in a real app.
    projects = [
        {"project_name": "Web App", "project_description": "A cool web app", "category": "web"},
        {"project_name": "Mobile App", "project_description": "A cool mobile app", "category": "mobile"},
        {"project_name": "Data Analysis", "project_description": "Data analysis project", "category": "data"}
    ]
    return jsonify(projects)
