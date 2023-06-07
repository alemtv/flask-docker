import unittest
from src import create_app
from flask import Flask
# from requests import get

class PublicCarsApiTests(unittest.TestCase):
    # Test unauthenticated API requests

    def setUp(self):
        # Create a test client for the app
        # self.app = create_app('DEV').test_client()
        self.app = Flask(__name__).test_client()
        # self.app = app.test_client()
        
    def test_app_creation(self):
        # app = create_app('DEV')
        # app.testing = True
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.name, '__main__')

    def test_retrieve_cars(self):
        # res = self.app.get('/cars')
        res = self.app.get('host.docker.internal:5000/cars')
        print(f'{res=}')
        self.assertEqual(res.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()