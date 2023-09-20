
from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import priority
from flask_app.models import user


@app.route("/priorities", methods=["POST"])
def add_priority():
    data = {
        "user_id": request.form["current_user"],
        "text": request.form["text"],
        "level": request.form["level"]
    }
    # VALIDATIONS COMING SOON:
    session["data"] = data
    if not priority.Priority.validate_priority(data):
        return redirect("/dashboard")
    session.pop("data")
    priority.Priority.save(data)
    return redirect("/dashboard")

@app.route('/priority/edit/<int:id>', methods=['POST'])
def process_edit_priority(id):
    if 'user_id' not in session:
        return redirect('/')
    if not priority.Priority.validate_priority(request.form):
        return redirect(f'/priority/edit/{id}')

    data = {
        'id': id,
        'text': request.form['text'],
        'level': request.form['level'],
    }
    priority.Priority.update(data)
    return redirect('/dashboard')

@app.route('/priority/destroy/<int:id>')
def destroy_priority(id):
    if 'user_id' not in session:
        return redirect('/')

    priority.Priority.destroy({'id':id})
    return redirect('/dashboard')
