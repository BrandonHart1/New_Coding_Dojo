from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def get_all(cls):
        print('*'*50)
        print('IN THE NINJA.GETALL METHOD')
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("dojos_ninjas_schema").query_db(query)
        ninjas = []

        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(age)s) NOW(), NOW() );"
        return connectToMySQL('dojos_ninjas_schema').query_db( query, data )