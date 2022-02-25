from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data),recipes=Recipe.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')








# from flask_app import app  

# from flask import render_template, redirect, session, request, flash
# from flask_app.models.user_model import User
# from flask_bcrypt import Bcrypt
# from flask import flash
# bcrypt = Bcrypt(app)

# # ----- Root route -----
# @app.route('/') # ----- The "@" decorator associates this route with the function immediately following -----
# def index():
#     return render_template('index.html')
# # ----- return the result of the render_template method, passing in the name of our HTML file -----

# # ----- Register new user and validate -----
# @app.route('/register', methods=['POST'])
# def register():
    
#     if not User.validate_new_user(request.form):
#         return redirect('/')

#     else:
#         data = {
#             'first_name': request.form['first_name'],
#             'last_name': request.form['last_name'],
#             'email': request.form['email'],
#             'password': bcrypt.generate_password_hash(request.form['password'])
            
#         }
#         print(data) # ----- check to see if bcrypt is working -----
#         User.create_new_user(data)
#         flash("Thank You For Registering!!!")
#         return redirect('/') 


# # ----- Login Page -----
# @app.route('/users/login', methods=['POST'])
# def user_login():
#     user = User.get_user_by_email(request.form)

#     if not user:
#         flash("Invalid Email/Password")
#         return redirect("/")
#     if not bcrypt.check_password_hash(user.password, request.form['password']):
#         # if we get False after checking the password
#         flash("Invalid Email/Password")
#         return redirect('/')

#     # if the passwords matched, we set the user_id into session
#     session['user_id'] = user.id
#     session['first_name'] = user.first_name    # <<<----- Storing the name into session -----

#     # print("____________________________________________________________________")
#     # print(session)
#     # never render on a post!!!
#     return redirect('/recipes')



# @app.route('/users/logout', methods=['POST'])
# def logout():

#     session.clear()

#     return redirect('/')



#     # if not User.get_user_by_email in session:
#     #     flash("Please log in")
#     #     return redirect('/')