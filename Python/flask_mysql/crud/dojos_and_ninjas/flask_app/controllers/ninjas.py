from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
        # -----  add the init  -----



@app.route("/")
def read_ninjas():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("view_ninjas.html", ninjas = ninjas)

@app.route("/new/ninja")
def create_ninja():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", dojos = dojos)

@app.route("/create/ninja", methods=["POST"])
def insert_ninja():
    data = {      
        "first_name": request.form["first_name"],    
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    ninja = Ninja.save(data)
    return redirect(f"/dojo/{request.form['dojo_id']}")
