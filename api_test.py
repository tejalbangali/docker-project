from flask import Flask
import pytest, unittest
import requests

# checking 200 response  
class apiTest(unittest.TestCase):
    def test_index(self):
        r = requests.get("http://127.0.0.1:8000/sign-up")
        self.assertEqual(r.status_code, 200)

# loginpage loads correctly
    def test_login_page(self):
        r = requests.get("http://127.0.0.1:8000/<usr>")
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

#run -> py.test api_test.py 
# or -> py.test/pytest