from flask_app.config.mysqlconnection import connectToMySQL

class Priority:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.level = data['level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO priorities(text, level)
        VALUES ( %(text)s, %(level)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_priorities(cls):
        all_priorities = []
        query = """
        SELECT * FROM priorities;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        for result in results:
            all_priorities.append(result)
        return all_priorities
