from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin

app = Flask(__name__, template_folder='/path/to/templates')
app.config['SECRET_KEY'] = 'your_secret_key_here'
login_manager = LoginManager(app)

# Example User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Example user database
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if current_user.is_authenticated:
        return f'Welcome to the dashboard, {current_user.id}!'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
