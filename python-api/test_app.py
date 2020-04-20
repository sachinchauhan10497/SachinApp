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
        test_jwt_tocken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3RpbmdfdXNlciJ9.se88Y8n4MxTRSVmC3UFVLOnTwYj5h1s_mN_tWSSP_L0"
        response = tester.get('/?userName=testing_user&jwt='+test_jwt_tocken, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("UTF-8"), "username = testing_user\nData : \ntesting_data")

    def test_register(self):
        """ Hitting Register API """
        tester = APP.test_client(self)
        url = '/register?userName=Rutu&password=rotadu'
        response = tester.post(url, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("UTF-8"), "This UserName Already exists.")
    
    def test_login(self):
        """ Hitting Login API """
        tester = APP.test_client(self)
        url = '/login?userName=Rutu&password=rotadu'
        response = tester.get(url, content_type="application/json")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
