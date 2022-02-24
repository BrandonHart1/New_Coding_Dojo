# from os import stat
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask import flash

class Recipe():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.recipe_date = data['recipe_date']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thiry']
        self.updated_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None


    @classmethod
    def create_recipe(cls, data):
            query = 'INSERT INTO recipes (name, recipe_date, description, instructions, under_thirty, user_id) VALUES (%(recipe_name)s, %(recipe_date)s, %(description)s, %(instructions)s, %(under_thirty)s, %(user_id)s);'

            results = connectToMySQL('recipes_schema').query_db(query, data)

            return results

    @classmethod
    def get_all_recipes(cls):

        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id'

        results = connectToMySQL("recipes_schema").query_db(query)

        recipes = []

        for item in results:
            new_recipe = Recipe(item)

            user_data = {
                'id': item['user_id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['last_name'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']

            }
            new_recipe.user = User(user_data)

            recipes.append(new_recipe)

        return recipes

    @classmethod
    def get_recipe_by_id(cls, data):

        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id = user_id WHERE recipes.id = %(id)s;'

        results = connectToMySQL('recipes_schema').query_db(query, data)

        recipe = Recipe(results[0])

        user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['last_name'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
        }
        recipe.user = User(user_data)
        return recipe


    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, recipe_date = %(recipe_date)s, description = %(description)s WHERE id = %(recipe_id)s;"

        results = connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'

        results = connectToMySQL('recipes_schema').query_db(query, data)

    @staticmethod
    def validate_new_recipe(data):
        is_valid = True

        if len(data['recipe_name']) < 3:
            is_valid = False
            flash("Recipe Name Must Be At Least 3 Characters")

        if len(data['description']) < 3:
            is_valid = False
            flash("Recipe Description Must Be At Least 3 Characters")

        if len(data['instructions']) < 3:
            is_valid = False
            flash("Recipe Instructions Must Be At Least 3 Characters")

        if data['recipe_date'] == "":
            is_valid = False
            flash("Date Cannot Be Blank")
        
        return is_valid



