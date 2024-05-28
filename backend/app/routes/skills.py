from flask import Blueprint, jsonify, request
from ..models import Skill, db

bp = Blueprint('skills', __name__)

@bp.route('/api/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return jsonify({'skills': [{'skill_name': skill.skill_name} for skill in skills]})

@bp.route('/api/skills', methods=['POST'])
def add_skill():
    data = request.json
    skill = Skill(skill_name=data['skill_name'])
    db.session.add(skill)
    db.session.commit()
    return jsonify({'message': 'Skill added successfully'})
