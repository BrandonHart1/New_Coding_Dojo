from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/ninjas")
def read():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("read.html", ninjas = ninjas)

# -----------------------------------------------------------------------------------

@app.route("/ninja/new")
def create_ninja():
    return render_template("create_ninja.html", dojos = Dojo.get_all())

# -----------------------------------------------------------------------------------

@app.route("/create/ninja", methods=["POST"])
def insert_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    ninja = Ninja.save(data)
    return redirect(f"/dojo/{request.form['dojo_id']}")
    