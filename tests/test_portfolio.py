 # tests/test_portfolio.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from backend.app import create_app, db

class PortfolioTestCase(unittest.TestCase):
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

    def test_get_portfolio(self):
        response = self.client.get('/api/portfolio')
        self.assertEqual(response.status_code, 404)

    def test_update_portfolio(self):
        response = self.client.post('/api/portfolio', json={'title': 'My Portfolio', 'description': 'My Description'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Portfolio updated successfully', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()