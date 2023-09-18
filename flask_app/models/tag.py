from flask_app.config.mysqlconnection import connectToMySQL

class Tag:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO tags(name, category_id)
        VALUES ( %(name)s, %(category_id)s)
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
