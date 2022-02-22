from flask_app.config.mysqlconnection import connectToMySQL

from flask import flask

class User():
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@staticmethod
def validate_new_user(data):
    is_valid = True

    email-regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if len(data['first_name']) < 2 or len(data)['"first_name'] > 50:
        is_valid = False
        flash('Name must be at least 2 characters')

    if not email_regex.match(data['email']):
        is_valid = False


    return is_valid