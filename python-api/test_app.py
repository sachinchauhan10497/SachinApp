from app import app
from flask import request

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_post(self):
    tester = app.test_client(self)
    response = tester.post('/?userName=testing_user&data=testing_data', content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_get(self):
    tester = app.test_client(self)
    response = tester.get('/?userName=testing_user', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.decode('UTF-8'),"testing_data")

if __name__ == '__main__':
    unittest.main()
