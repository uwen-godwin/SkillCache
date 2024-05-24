from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_name = db.Column(db.String(80), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_name = db.Column(db.String(120), nullable=False)
    project_description = db.Column(db.Text, nullable=False)

@app.route('/api/portfolio', methods=['GET', 'POST'])
def portfolio():
    if request.method == 'GET':
        return jsonify({"message": "Get portfolio data"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Add/update portfolio data", "data": data})

@app.route('/api/skills', methods=['GET', 'POST'])
def skills():
    if request.method == 'GET':
        return jsonify({"message": "Get skills list"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Add new skill", "data": data})

@app.route('/api/projects', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        return jsonify({"message": "Get projects list"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Add new project", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
