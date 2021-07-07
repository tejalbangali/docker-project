import json
from flask import Flask, render_template
from flask import request, redirect, url_for

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


# open cmd in file then start app by-cmd -> python name.py
# or do same in terminal by cmd -> python name.py
