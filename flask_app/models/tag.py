from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import link, priority

class Tag:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.user_id = data['user_id']
        self.priorities = []
        self.links = []

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO tags(name, category_id, user_id)
        VALUES ( %(name)s, %(category_id)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_tags(cls):
        all_tags = []
        query = """
        SELECT * FROM tags;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        for result in results:
            all_tags.append(result)
        return all_tags

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM tags
        WHERE tags.id = %(tag_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)[0]

    @classmethod
    def get_tag_links(cls, data):
        tag_links = []
        query = """
        SELECT * FROM links
        JOIN tag_links ON tag_links.link_id = links.id
        JOIN tags ON tags.id = tag_links.tag_id
        JOIN link_types ON link_types.id = links.link_type_id
        WHERE tags.id = %(tag_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            current_link_data = {
                "id": result["id"],
                "text": result["text"],
                "url": result["url"],
                "description": result["description"],
                "created_at": result["created_at"],
                "updated_at": result["updated_at"],
                "link_type_id": result["link_type_id"],
                "user_id": result["user_id"]
            }
            current_link = link.Link(current_link_data)
            tag_links.append(current_link)
        return tag_links

    @classmethod
    def get_tag_priorities(cls, data):
        tag_priorities = []
        query = """
        SELECT * FROM priorities
        JOIN tag_priorities ON tag_priorities.priority_id = priorities.id
        WHERE tag_priorities.tag_id = %(tag_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            current_priority_data = {
                "id": result["id"],
                "text": result["text"],
                "level": result["level"],
                "created_at": result["created_at"],
                "updated_at": result["updated_at"],
                "user_id": result["user_id"]
            }
            current_priority = priority.Priority(current_priority_data)
            tag_priorities.append(current_priority)
        return tag_priorities
