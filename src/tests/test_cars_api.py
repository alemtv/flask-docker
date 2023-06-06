from unittest import TestCase
from src import create_app

class PublicCarsApiTests(TestCase):
    # Test unauthenticated API requests

    def setUp(self):
        # Create a test client for the app
        self.app = create_app('DEV').test_client()\
        
    def test_app_creation(self):
        # app = create_app('DEV')
        # app.testing = True
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.name, '__main__')

    def test_retrieve_cars(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()