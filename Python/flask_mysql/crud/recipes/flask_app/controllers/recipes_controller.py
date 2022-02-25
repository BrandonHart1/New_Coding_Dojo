from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User


@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_recipe.html', user = User.get_by_id(data))

@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "recipe_date": request.form["recipe_date"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/recipe',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "recipe_date": request.form["recipe_date"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_recipe.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')







# @app.route('/recipes')
# def recipes():
#     recipes = Recipe.get_all_recipes()
#     #get all recipes from database
#     return render_template('recipes.html', recipes = recipes)

# @app.route('/recipes/new')
# def new_recipe():
#     return render_template('new_recipe.html')


# @app.route('/recipes/create', methods=['POST'])
# def create_recipe():

#     if not Recipe.validate_new_recipe(request.form):
#         return redirect('/recipes/new')

#     data = {
#         'recipe_name': request.form['recipe_name'],
#         'recipe_date': request.form['recipe_date'],
#         'description': request.form['description'],
#         'instructions': request.form['instructions'],

#         'user_id': session['user_id']
        
#     }
#     return redirect('/recipes')

# @app.route('/recipes/<int:recipe_id>')
# def single_recipe(recipe_id):
#     data = {
#         'id': recipe_id
#     }
#     recipe = Recipe.get_recipe_by_id(data)
    
#     return render_template('single_recipe.html', recipe = recipe)

# @app.route('/recipes/<int:recipe_id>/edit')
# def edit_recipe(recipe_id):
#     data = {
#         'id': recipe_id
#     }
#     recipe = Recipe.get_recipe_by_id(data)
#     if session['user_id'] != recipe.user_id:
#         return redirect ('/recipes')
#     recipe = Recipe.get_recipe_by_id(data)
#     print(type(recipe.date))
#     recipe.date = str(recipe.date)[0:10]
#     return render_template('recipe_edit.html', recipe = recipe)
    

# @app.route('/recipes/<int:recipe_id>/update', methods=["POST"])
# def update_recipe(recipe_id):

#     if not Recipe.validate_new_recipe(request.form):
#         return redirect(f'/shows/{recipe_id}/edit')

#     else:
#         data = {
#             'recipe_id': recipe_id,
#             'name': request.form['name'],
#             'date': request.form['date'],
#             'description': request.form['description']

#         }
#         Recipe.update_recipe(data)
#         return redirect(f'/recipes/{recipe_id}')


# @app.route('/recipes/<int:recipe_id>/delete')
# def delete(recipe_id):
#     data = {
#         'id': recipe_id
#     }

#     recipe = Recipe.get_recipe_by_id(data)
#     return redirect('/recipes')