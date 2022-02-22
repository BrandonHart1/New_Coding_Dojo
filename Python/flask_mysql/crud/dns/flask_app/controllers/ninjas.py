from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas/new')
def ninjas_new():
    dojos = Dojo.get_all()
    return render_template('ninjas_new.html', dojos = dojos)

@app.route('/ninjas/insert', methods=['POST'])
def ninjas_insert():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    print("*******************************")
    print(data)
    dojo_id = request.form['dojo_id']
    Ninja.insert(data)
    return redirect(f'/dojos/{dojo_id}')