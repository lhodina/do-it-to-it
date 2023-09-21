from flask import render_template, redirect, session

from flask_app import app
from flask_app.models import tag

@app.route("/tags/<int:tag_id>")
def get_tag_page(tag_id):
    if session and session["current_user"]:
        data = {
            "user_id": session["current_user"]["id"],
            "tag_id": tag_id
        }
        current_tag = tag.Tag.get_one(data)
        print("current_tag in controller: ", current_tag)
        tag_links = tag.Tag.get_tag_links(data)
        print("tag_links in controller: ", tag_links)
        current_tag['links'] = tag_links
        for tag_link in current_tag['links']:
            print("tag_link.id: ", tag_link.id)
            print("tag_link.text: ", tag_link.text)
            print("tag_link.url: ", tag_link.url)
            print("tag_link.description: ", tag_link.description)
            print("tag_link.link_type_id: ", tag_link.link_type_id)
            print()
        tag_priorities = tag.Tag.get_tag_priorities(data)

        # for tag_priority in tag_priorities:
        #     print("tag_priority.id: ", tag_priority.id)
        #     print("tag_priority.text: ", tag_priority.text)
        #     print("tag_priority.level: ", tag_priority.level)
        return render_template("view.html", current_tag=current_tag, tag_links=current_tag['links'], tag_priorities=tag_priorities)
    else:
        return redirect("/dashboard")
