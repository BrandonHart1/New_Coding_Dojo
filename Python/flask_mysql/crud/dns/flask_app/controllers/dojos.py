from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojos/new')
def dojos_new():
    return render_template('dojos_new.html')

@app.route('/dojos/insert', methods=['POST'])
def dojos_insert():
    data = {
        'dojo_name': request.form['dojo_name']
    }
    Dojo.insert(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojo_display(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_one_dojo_with_ninjas(data)
    return render_template('dojo_display.html', dojo = dojo)

