from flask import Flask, request, redirect, render_template
import cgi
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    errors = False
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    matching_error = ""

    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    if len(password) <3 or len(password) >20:
        password_error = "That's not a valid password"

    if len(verify) <3 or len(verify) >20:
        verify_error = "That's not a valid password"

    if not verify == password:
        matching_error = "Passwords don't match"

    if email.count("@") != 1 or email.count(".") != 1:
        email_error = "That's not a valid email"

    if not username_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template("index.html", username = username, email = email, password = password, verify = verify,
            username_error = username_error, password_error = password_error,
            verify_error = verify_error, email_error = email_error, matching_error = matching_error)
    return validate

@app.route("/")
def index():
    return render_template("index.html")

app.run()
