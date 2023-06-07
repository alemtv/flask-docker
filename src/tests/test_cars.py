import unittest
from flask import Flask
import requests

class PublicCarsApiTests(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app client for testing
        self.app = Flask(__name__)

    def test_retrieve_cars(self):
        # Make a request to the Flask app running in the Docker container
        base_url = 'http://172.19.0.3:5000'
        endpoint = '/cars'
        url = base_url + endpoint

        # response = self.app.get('/cars')
        response = requests.get(url)
        print(f'{response=}')

        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()