import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from backend import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
