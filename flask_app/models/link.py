from flask_app.config.mysqlconnection import connectToMySQL

class Link:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.url = data['url']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.link_type_id = data['link_type_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO links(text, url, description, user_id)
        VALUES ( %(text)s, %(url)s, %(description)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_user_links(cls, data):
        all_links = []
        query = """
        SELECT * FROM links
        WHERE user_id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_links.append(result)
        return all_links

    @classmethod
    def get_all_link_types(cls, data):
        all_link_types = []
        query = """
        SELECT * FROM link_types;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_link_types.append(result)
        return all_link_types