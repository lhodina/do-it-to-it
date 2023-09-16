from flask import render_template

from flask_app import app

@app.route("/dashboard")
def go_to_dashboard():
    return render_template("dashboard.html")
