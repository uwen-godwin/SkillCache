 # tests/test_projects.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from backend.app import create_app, db

class ProjectsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_projects(self):
        response = self.client.get('/api/projects')
        self.assertEqual(response.status_code, 404)

    def test_add_project(self):
        response = self.client.post('/api/projects', json={'project_name': 'Project X', 'project_description': 'Description'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Project added successfully', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()