
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
    #     return redirect("/dashboard")
    # session.pop("data")
    priority.Priority.save(data)
    return redirect("/dashboard")


@app.route("/priorities/update", methods=["POST"])
def update_priority():
    data = {
        "id": request.form["prio_select"],
        "text": request.form["text"],
        "level": request.form["level"]
    }
    priority.Priority.update(data)
    return redirect("/dashboard")


@app.route("/priorities/<int:priority_id>/delete")
def delete_priority(priority_id):
    data = {"id": priority_id}
    priority.Priority.destroy(data)
    return redirect("/dashboard")


@app.route('/priorities/<int:priority_id>/add_tag', methods=["POST"])
def add_tag_to_priority(priority_id):
    data = {
    "priority_id": priority_id,
    "tag_id": request.form["tag_id"]
    }
    priority.Priority.add_tag(data)
    return redirect("/dashboard")
