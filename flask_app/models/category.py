from flask_app.config.mysqlconnection import connectToMySQL

class Category:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO categories(name, user_id)
        VALUES ( %(name)s, %(user_id)s)
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

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM categories
        WHERE categories.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        print("***** result: ", result)
        # current_show_data = {
        #     "id": result["id"],
        #     "title": result["title"],
        #     "network": result["network"],
        #     "release_date": result["release_date"],
        #     "description": result["description"],
        #     "created_at": result["created_at"],
        #     "updated_at": result["updated_at"],
        #     "user_id": result["user_id"]
        # }
        return result
