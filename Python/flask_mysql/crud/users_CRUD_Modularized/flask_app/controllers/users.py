from flask import render_template, request, redirect

from flask_app.models.user import User

from flask_app import app



@app.route("/")
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", users = users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/insert", methods=["POST"])
def insert():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')