import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to the Flask app!")

    def test_greet(self):
        response = self.app.get('/api/greet/John')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, John!", response.get_json()['message'])


if __name__ == '__main__':
    unittest.main()
