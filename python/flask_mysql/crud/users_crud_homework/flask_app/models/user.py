from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'users_crud'
    def __init__(self,data):
        self.id=data['id']
        self.username=data['username']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def createUser(cls,data):
        query = 'INSERT INTO users (username, email, password) VALUES ( %(username)s, %(email)s, %(password)s );'
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def getAllUsers(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.db_name).query_db(query)
        users=[]
        if results:
            for eachUser in results:
                users.append(eachUser)
        return users