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

# -----------------------------------------------------------------------------
# ----- Make sure user info is valid -----


    @classmethod
    def create_new_user(cls, data):
        #----- Inserting the record into the database -----
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL("users_exam").query_db(query, data) 


    @classmethod
    def get_user_by_email(cls, data):
        # ----- Running a query to get all users by email -----
        query = "SELECT * FROM users WHERE email = %(email)s"   
        results = connectToMySQL("users_exam").query_db(query, data)
        
        # ----- if the user doesn't exist, add to db.  If user exists, don't add to db.

        if len(results) < 1:   # Length needs to be 1 or more.
            return False
            

        return User(results[0])  # ----- return a new instance of the User class -----

# ---------- Validate that the user isn't already in use ----------
    @staticmethod
    def validate_new_user(data):
        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# ----- Validate a valid name and password -----
        if len(data['first_name']) < 2:
            is_valid = False
            flash('First Name needs to be at least 2 characters')

        if len(data['last_name']) < 2:
            is_valid = False
            flash('Last Name needs to be at least 2 characters')

        if len(data['password']) < 8:
            is_valid = False
            flash('Password needs to be at least 8 characters')

        # ----- if email is/isn't available -----
        if User.get_user_by_email(data):
            is_valid = False
            flash("Email is Already Taken")

        if not email_regex.match(data['email']):
            is_valid = False
            flash('Email Format is Invalid')

        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password Needs To Be the Same")


        return is_valid



        # -----------------------------------------------------------------------------
# [x] No matter the email, it comes up as "Email Already Exists" (Fixed)
# [x] Only receiving one flash for multiple problem on Register (Maybe Fixed)
# [x] Login page doesn't route to success page
# [x] New register not showing up in the db