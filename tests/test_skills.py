 # tests/test_skills.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from backend.app import create_app, db

class SkillsTestCase(unittest.TestCase):
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

    def test_get_skills(self):
        response = self.client.get('/api/skills')
        self.assertEqual(response.status_code, 404)

    def test_add_skill(self):
        response = self.client.post('/api/skills', json={'skill_name': 'Python'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Skill added successfully', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main() 