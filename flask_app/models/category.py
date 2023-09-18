from flask_app.config.mysqlconnection import connectToMySQL

class Category:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO categories(name)
        VALUES ( %(name)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_categories(cls):
        all_categories = []
        query = """
        SELECT * FROM categories;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        for result in results:
            all_categories.append(result)
        return all_categories
