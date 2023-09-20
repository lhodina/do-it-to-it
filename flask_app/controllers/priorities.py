
from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models import priority


@app.route("/priorities", methods=["POST"])
def add_priority():
    data = {
        "user_id": request.form["current_user"],
        "text": request.form["text"],
        "level": request.form["level"]
    }
    # VALIDATIONS COMING SOON:
    # session["data"] = data
    # if not priority.Priority.validate_priority(data):
    #     return redirect("/priorities/new")
    # session.pop("data")
    priority.Priority.save(data)
    return redirect("/dashboard")
