from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db_name='dojosninjas'
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.dojo_id=data['dojo_id']

    @classmethod
    def createNinja(cls,data):
        query = 'INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);'
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def getAllNinjas(cls,data):
        query='SELECT * FROM ninjas where dojo_id = %(id)s;'
        results= connectToMySQL(cls.db_name).query_db(query,data)
        ninjas=[]
        if results:
            for ninja in results:
                ninjas.append(ninja)
        return ninjas