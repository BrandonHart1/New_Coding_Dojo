from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/')
def read_dojos():
    dojos = Dojo.get_all()
    print("######################################")
    print(dojos)
    return render_template("show_dojo.html", dojos = dojos)

# ----------------------------------------------------------------

@app.route('/dojo/new')
def create_dojo():
    return render_template("create_dojo.html")

# -----------------------------------------------------------------

@app.route('/create/dojo', methods=["POST"])
def insert_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save_dojo(data)
    return redirect(f"/dojo/{request.form['dojo_id']}")

# ------------------------------------------------------------------

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_one(data)
    print(dojo)
    return render_template('read.html', dojo = dojo)