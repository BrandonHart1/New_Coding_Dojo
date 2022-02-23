from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import users
from flask import flash

import re

class User():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        result = connectToMySQL("login_reg").query_db(query, data)


    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"

        results = connectToMySQL("login_reg").query_db(query, data)
        
        # ----- if the user doesn't exist, add to db.  If user exists, don't add to db.

        if len(results) == 0:
            return False
            
        else:
            return User(results[0])  # ----- return a new instance of the User class -----


    @staticmethod
    def validate_new_user(data):
        is_valid = True

        # if email is/isn't available
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


        if len(data['first_name']) < 2:
            is_valid = False
            flash('First Name needs to be at least 2 characters')

        if len(data['last_name']) < 2:
            is_valid = False
            flash('Last Name needs to be at least 2 characters')

        if len(data['password']) < 8:
            is_valid = False
            flash('Password needs to be at least 8 characters')

        if User.get_user_by_email(data):
            is_valid = False
            flash("Email is Already Taken")

        if not email_regex.match(data['email']):
            is_valid = False
            flash('Email Format is Invalid')

        if not data['password'] == data['confirm_password']:
            is_valid = False


        return is_valid