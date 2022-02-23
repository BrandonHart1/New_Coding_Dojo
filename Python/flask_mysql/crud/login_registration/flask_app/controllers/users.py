from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    
    if not User.validate_new_user(request.form):
        return redirect('/')

    if not User.get_user_by_email(request.form):
        flash("This Email Already Exists")
        return redirect('/')

    
    else:
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
            
        }
        print(data) # ----- check to see if bcrypt is working -----
        User.create_new_user(data)
        flash("Thank You For Registering!!!")
        return redirect('/') 

@app.route('/users/login', methods=['POST'])
def user_login():
    user = User.get_user_by_email(request.form)

    if not bcrypt.generate_password_hash(request.form['password']):
        flash("Password is Incorrect.")


    return redirect ('/success')

@app.route('/success')
def seccess():
    
    if not User.get_user_by_email in session:
        flash("Please log in")
        return redirect('/')
    return render_template('success.html')


@app.route('/users/logout')
def logout():
    session.clear()

    return redirect('/')