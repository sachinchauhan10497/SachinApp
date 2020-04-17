""" Unit test GET and POST APs """

import unittest
from app import APP

class AppTestCase(unittest.TestCase):
    """ Testing Flask App """

    def test_post(self):
        """ Hitting POST API """
        tester = APP.test_client(self)
        post_url = "/?userName=testing_user&data=testing_data"
        response = tester.post(post_url, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        """ Hitting GET API """
        tester = APP.test_client(self)
        response = tester.get('/?userName=testing_user', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("UTF-8"), "testing_data")

if __name__ == "__main__":
    unittest.main()
