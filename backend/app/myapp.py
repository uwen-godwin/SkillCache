from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.sqlite3'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Database Models
class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Portfolio(db.Model):
    portfolio_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Skill(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    skill_name = db.Column(db.String(50), nullable=False)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    project_name = db.Column(db.String(80), nullable=False)
    project_description = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, '../frontend'), 'index.html')

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory(os.path.join(app.root_path, '../frontend/static'), path)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/api/portfolio', methods=['GET', 'POST'])
def portfolio():
    if request.method == 'GET':
        portfolios = Portfolio.query.all()
        return jsonify([{
            'portfolio_id': p.portfolio_id,
            'user_id': p.user_id,
            'title': p.title,
            'description': p.description
        } for p in portfolios])
    if request.method == 'POST':
        data = request.json
        new_portfolio = Portfolio(user_id=data['user_id'], title=data['title'], description=data['description'])
        db.session.add(new_portfolio)
        db.session.commit()
        return jsonify({'message': 'Portfolio added successfully'})

@app.route('/api/skills', methods=['GET', 'POST'])
def skills():
    if request.method == 'GET':
        skills = Skill.query.all()
        return jsonify([{
            'skill_id': s.skill_id,
            'user_id': s.user_id,
            'skill_name': s.skill_name
        } for s in skills])
    if request.method == 'POST':
        data = request.json
        new_skill = Skill(user_id=data['user_id'], skill_name=data['skill_name'])
        db.session.add(new_skill)
        db.session.commit()
        return jsonify({'message': 'Skill added successfully'})

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        projects = Project.query.all()
        return jsonify([{
            'project_id': p.project_id,
            'user_id': p.user_id,
            'project_name': p.project_name,
            'project_description': p.project_description
        } for p in projects])
    if request.method == 'POST':
        data = request.json
        new_project = Project(user_id=data['user_id'], project_name=data['project_name'], project_description=data['project_description'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project added successfully'})

@app.route('/api/job_search', methods=['POST'])
def job_search():
    search_params = request.json
    response = requests.post('https://jobs.github.com/positions.json', params=search_params)
    return jsonify(response.json())

@app.route('/api/user_info', methods=['GET'])
def user_info():
    linkedin_user_info = {}  # Fetch from LinkedIn API
    return jsonify(linkedin_user_info)

if __name__ == '__main__':
    app.run(debug=True)
