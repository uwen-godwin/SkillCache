from flask import Blueprint, jsonify

bp = Blueprint('skills', __name__, url_prefix='/api/skills')

@bp.route('/', methods=['GET'])
def get_skills():
    # This is just a placeholder. You would fetch from the database in a real app.
    skills = [
        {"skill_name": "Python"},
        {"skill_name": "JavaScript"},
        {"skill_name": "HTML/CSS"}
    ]
    return jsonify(skills)
