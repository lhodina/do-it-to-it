from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Priority:
    DB = "do_it_to_it"
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.level = data['level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO priorities(text, level, user_id)
        VALUES ( %(text)s, %(level)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM priorities
                JOIN users on priorities.user_id = users.id
                WHERE priorities.id = %(id)s;
                """
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return False

        result = result[0]
        this_priority = cls(result)
        user_data = {
                "id": result['users.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": "",
                "created_at": result['users.created_at'],
                "updated_at": result['users.updated_at']
        }
        this_priority.creator = user.User(user_data)
        return this_priority

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
                level = %(level)s,
                updated_at = now()
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
    
    @staticmethod
    def validate_priority(form_data):
        is_valid = True

        if len(form_data['text']) < 2:
            flash("Description must be at least 2 characters long.")
            is_valid = False
        if len(form_data['level']) < 1:
            flash("must have priority level.")
            is_valid = False
        return is_valid
