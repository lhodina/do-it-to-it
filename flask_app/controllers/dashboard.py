from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models import category, tag, priority, link


@app.route("/dashboard")
def go_to_dashboard():
    if session and session["current_user"]:
        data = {
            "id": session["current_user"]["id"]
        }
        print("data: ", data)
        all_user_priorities = priority.Priority.get_all_user_priorities(data)
        all_user_links = link.Link.get_all_user_links(data)
        all_categories = category.Category.get_all_categories()
        all_tags = tag.Tag.get_all_tags()
        all_link_types = link.Link.get_all_link_types(data)
        print("***** all_categories: ", all_categories)
        print()
        print("***** all_tags: ", all_tags)
        print()
        print("***** all_user_priorities: ", all_user_priorities)
        print()
        print("***** all_user_links: ", all_user_links)
        return render_template("dashboard.html", all_user_priorities=all_user_priorities, all_categories=all_categories, all_tags=all_tags, all_user_links=all_user_links, all_link_types=all_link_types)
    else:
        return redirect("/")
