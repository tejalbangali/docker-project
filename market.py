# open cmd in file then start app by-cmd -> python name.py
# or do same in terminal by cmd -> python name.py


from flask import Flask, render_template, request, redirect, url_for
import pytest, unittest, json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        req = request.form
        username = req['username']
        email = req.get('email')
        password = req['password']
        print(username, email, password)
        user = username, email
        return redirect(url_for('user',usr=user))
    else:
        return render_template('sign-up.html')

@app.route('/<usr>')
def user(usr):
    return f"<h3>Welcome {usr}</h3>"

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

# checking 200 response  ***cmd: pytest market.py
class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        self.assertEqual(response.status_code, 200)

# loginpage loads correctly
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up')
        self.assertTrue(b'Please Login' in response.data)

if __name__ == '__main__':
    unittest.main()

#to start
# set FLASK_APP=market.py
# set FLASK_DEBUG=1
# flask run