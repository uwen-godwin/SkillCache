from flask import Flask, request, jsonify

app = Flask(__name__)

# Define your database models and routes here
# ...

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to my Flask application!'

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
