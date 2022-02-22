from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        

    @classmethod
    def get_all(cls):
        # print('*'*50)
        # print('IN THE NINJA.GETALL METHOD')
        query = "SELECT * FROM ninjas"
        results = connectToMySQL("dns").query_db(query)
        ninjas = []

        for ninja in results:
            ninjas.append( Ninja(ninja) )
        return ninjas

    @classmethod
    def insert(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dns').query_db( query, data )


        