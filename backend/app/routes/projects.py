from flask import Blueprint, jsonify, request
from ..models import Project, db

bp = Blueprint('projects', __name__)

@bp.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify({'projects': [{'project_name': project.project_name, 'project_description': project.project_description} for project in projects]})

@bp.route('/api/projects', methods=['POST'])
def add_project():
    data = request.json
    project = Project(project_name=data['project_name'], project_description=data['project_description'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'message': 'Project added successfully'})
