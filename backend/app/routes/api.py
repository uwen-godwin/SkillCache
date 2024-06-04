from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app import db
from app.models import Portfolio, Skill, Project

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():
    if request.method == 'GET':
        portfolios = Portfolio.query.filter_by(user_id=current_user.user_id).all()
        return jsonify([{
            'portfolio_id': p.portfolio_id,
            'user_id': p.user_id,
            'title': p.title,
            'description': p.description
        } for p in portfolios])
    if request.method == 'POST':
        data = request.json
        new_portfolio = Portfolio(user_id=current_user.user_id, title=data['title'], description=data['description'])
        db.session.add(new_portfolio)
        db.session.commit()
        return jsonify({'message': 'Portfolio added successfully'})

@bp.route('/skills', methods=['GET', 'POST'])
@login_required
def skills():
    if request.method == 'GET':
        skills = Skill.query.filter_by(user_id=current_user.user_id).all()
        return jsonify([{
            'skill_id': s.skill_id,
            'user_id': s.user_id,
            'skill_name': s.skill_name
        } for s in skills])
    if request.method == 'POST':
        data = request.json
        new_skill = Skill(user_id=current_user.user_id, skill_name=data['skill_name'])
        db.session.add(new_skill)
        db.session.commit()
        return jsonify({'message': 'Skill added successfully'})

@bp.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    if request.method == 'GET':
        projects = Project.query.filter_by(user_id=current_user.user_id).all()
        return jsonify([{
            'project_id': p.project_id,
            'user_id': p.user_id,
            'project_name': p.project_name,
            'project_description': p.project_description
        } for p in projects])
    if request.method == 'POST':
        data = request.json
        new_project = Project(user_id=current_user.user_id, project_name=data['project_name'], project_description=data['project_description'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully'})

@bp.route('/job_search', methods=['POST'])
def job_search():
    search_params = request.json
    response = requests.post('https://jobs.github.com/positions.json', params=search_params)
    return jsonify(response.json())

@bp.route('/user_info', methods=['GET'])
def user_info():
    linkedin_user_info = {}  # Fetch from LinkedIn API
    return jsonify(linkedin_user_info)
