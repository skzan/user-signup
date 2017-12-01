from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True


def is_invalid(text):
    return re.search(r'\s+', text) or re.search(r'^.{0,2}$', text) or re.search(r'^\w{20}', text)


@app.route("/", methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if is_invalid(username):
        username = ""
        username_error = "That's not a valid username"

    if is_invalid(password):
        password = ""
        password_error = "That's not a valid password"

    if verify == "":
        verify_error = "Passwords don't match"

    if verify != password:
        verify = ""
        verify_error = "Passwords don't match"

    if email != "" or (email.count("@") != 1 or email.count(".") != 1 or is_invalid(email)):
        email_error = "That's not a valid email"

    if username_error !="" and password_error !="" and verify_error !="" and email_error !="":
        return redirect("/welcome?username=" + username)
    else:
        template = jinja_env.get_template("index.html")
        return render_template("index.html", username = username, email = email,
            username_error = username_error, password_error = password_error,
            verify_error = verify_error, email_error = email_error)


@app.route("/")
def index():
    template = jinja_env.get_template("index.html")
    return render_template("index.html")


@app.route("/welcome")
def welcome():
    template = jinja_env.get_template("welcome.html")
    username = request.args.get("username")
    return render_template(username=username)


app.run()
