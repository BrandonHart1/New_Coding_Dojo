import re
from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL

class Show():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.network = data['network']
        self.release_date= data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None # Need instance of the user object


    # ----- send to database -----
    @classmethod
    def create_show(cls, data):

        query = "INSERT INTO shows (name, network, release_date, description, created_at, updated_at, user_id) VALUES (%(name)s, %(network)s, %(release_date)s, %(description)s, NOW(), NOW(), %(user_id)s)"

        result = connectToMySQL("users_exam").query_db(query, data)

        return result

    # ----- Get all shows -----
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id;"

        results = connectToMySQL("users_exam").query_db(query)

        shows = []

        for item in results:
            new_show = Show(item)

            user_data = {
                "id": item['users.id'],
                "first_name": item["first_name"],
                "last_name": item['last_name'],
                "email": item['email'],
                "password": item['password'],
                "created_at": item['created_at'],
                "updated_at": item['updated_at']

            }
            new_show.user = User(user_data)

            shows.append(new_show)

        return shows

    @classmethod
    def get_show_by_id(cls, data):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"
    
        result = connectToMySQL("users_exam").query_db(query, data)

        show = Show(result[0])

        user_data = {
            "id": result[0]['users.id'],
                "first_name": result[0]["first_name"],
                "last_name": result[0]['last_name'],
                "email": result[0]['email'],
                "password": result[0]['password'],
                "created_at": result[0]['created_at'],
                "updated_at": result[0]['updated_at']
        }
        show.user = User(user_data)
        return show

# ----- Update Show -----

    @classmethod
    def update_show(cls, data):
        query = 'UPDATE shows SET name = %(name)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s'

        result = connectToMySQL("users_exam").query_db(query, data)



# ----- validate new show -----
    @staticmethod
    def validate_new_show(data):
        is_valid = True
        
        if len(data['show_name']) < 3:
            is_valid = False
            flash('Title Should Be At Least 3 Character')

        if len(data['network']) < 3:
            is_valid = False
            flash('Title Should Be At Least 3 Character')

        if len(data['description']) < 3:
            is_valid = False
            flash('Title Should Be At Least 3 Character')

        return is_valid


    # --------------- Delete -----------
    @classmethod
    def delete_show(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL('users_exam').query_db(query,data)
