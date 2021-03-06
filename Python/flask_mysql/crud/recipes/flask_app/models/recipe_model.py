from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    name = 'recipes'

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.recipe_date = data['recipe_date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, under30, recipe_date, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under30)s,%(recipe_date)s,%(user_id)s);"
        return connectToMySQL('recipe_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL('recipe_schema').query_db(query)
        all_recipes = []
        for row in results:
            print(row['recipe_date'])
            all_recipes.append( cls(row) )
        return all_recipes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipe_schema').query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under30=%(under30)s, recipe_date=%(recipe_date)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipe_schema').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipe_schema').query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['recipe_date'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid
