from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    db_name = 'dojosninjas'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def createDojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(cls.db_name).query_db(query,data) 
    
    @classmethod
    def getAllDojos(cls):
        query = 'SELECT id, name FROM dojos;'
        results = connectToMySQL(cls.db_name).query_db(query)
        dojos=[]
        if results:
            for eachDojo in results:
                dojos.append(eachDojo)
        return dojos
    
    @classmethod
    def get_dojo_by_id(cls,data):
        query = "SELECT * FROM dojos where id=%(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if results:
            return results[0]
        return False