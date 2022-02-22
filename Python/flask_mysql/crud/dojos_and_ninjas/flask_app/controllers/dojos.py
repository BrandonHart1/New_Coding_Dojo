from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
        # -----  add the init???  -----



@app.route("/dojos")
def read_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("view_dojos.html", dojos = dojos)

@app.route("/new/dojo")
def create():
    return render_template("create_dojo.html")

@app.route("/create/dojo", methods=["POST"])
def insert_dojo():
    # data = {
        # "name": request.form["name"]
    # }
    Dojo.save_dojo(request.form)
    return redirect("/dojos")

@app.route("/dojo/<id>")
def show_dojo(dojo_id):
    return render_template("show_dojo.html")
