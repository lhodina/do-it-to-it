from flask_app.config.mysqlconnection import connectToMySQL

class Priority:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.level = data['level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO priorities(text, level, user_id)
            VALUES ( %(text)s, %(level)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_user_priorities(cls, data):
        all_user_priorities = []
        query = """
            SELECT * FROM priorities
            WHERE(user_id = %(id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        for result in results:
            all_user_priorities.append(result)
        return all_user_priorities

    @classmethod
    def update(cls,form_data):
        query = """
                UPDATE priorities
                SET text = %(text)s,
                level = %(level)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query,form_data)

    @classmethod
    def destroy(cls,data):
        query = """
                DELETE FROM priorities
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query,data)
