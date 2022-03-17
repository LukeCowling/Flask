from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("home.html", text="Logout")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        userName = request.form.get("userName")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(userName) < 1:
            flash("Please enter a username", category="error")
        elif len(firstName) < 1:
            flash("Please enter a name", category="error")
        elif len(password1) < 1:
            flash("Please enter a password", category="error")
        elif password1 != password2:
            flash("The passwords do not pamtch", category="error")
        else:
            flash("Account created", category="success")
    return render_template("sign_up.html")
