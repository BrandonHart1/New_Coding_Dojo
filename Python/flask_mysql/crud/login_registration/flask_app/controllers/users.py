from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

# ----- Root route -----
@app.route('/')
def index():
    return render_template('index.html')


# ----- Register new user and validate -----
@app.route('/register', methods=['POST'])
def register():
    
    if not User.validate_new_user(request.form):
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


# ----- Login Page -----
@app.route('/users/login', methods=['POST'])
def user_login():
    user = User.get_user_by_email(request.form)

    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    # print("____________________________________________________________________")
    # print(session)
    # never render on a post!!!
    return redirect("/success")

# ----- Success Page -----
@app.route('/success')
def success():
    
    # ----- checking if the key 'user id' is in session
    if not 'user_id' in session:
        return redirect('/')

    return render_template('success.html')


@app.route('/users/logout', methods=['POST'])
def logout():

    session.clear()

    return redirect('/')



    # if not User.get_user_by_email in session:
    #     flash("Please log in")
    #     return redirect('/')