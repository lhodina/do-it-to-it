from flask import render_template

from flask_app import app
from flask_app.models import category, tag, priority


@app.route("/dashboard")
def go_to_dashboard():
    all_priorities = priority.Priority.get_all_priorities()
    all_categories = category.Category.get_all_categories()
    all_tags = tag.Tag.get_all_tags()
    print("***** all_categories: ", all_categories)
    print()
    print("***** all_tags: ", all_tags)
    print()
    print("***** all_priorities: ", all_priorities)
    return render_template("dashboard.html", all_priorities=all_priorities, all_categories=all_categories, all_tags=all_tags)
