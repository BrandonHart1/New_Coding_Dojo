from flask_app import app

from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.show import Show

@app.route('/shows')
def shows():
    if "user_id" not in session:
        return redirect('/')
    shows = Show.get_all_shows()
    print(shows)

    return render_template('shows.html', shows = shows)


# --------------------- Render New Show Template --------------------

@app.route('/shows/new')
def new_show():
    
    return render_template('new_show.html')


# ------------- Validate new show ------------

@app.route('/shows/create', methods=['POST'])
def create_show():

    if not Show.validate_new_show(request.form):
        return redirect('/shows/new')

    data = {
        "name": request.form['show_name'],
        "network": request.form["network"],
        "release_date": request.form['release_date'],
        "description": request.form['description'],
        "user_id": session["user_id"]
    }

    Show.create_show(data)
    return redirect('/shows')

# --------------------- Show a single show --------------------


@app.route('/shows/<int:show_id>')
def single_show(show_id):

    data = {
        'id': show_id
    }

    show = Show.get_show_by_id(data)
    return render_template('single_show.html', show = show)

# --------------------- Edit Show --------------------

@app.route('/edit_show/<int:show_id>')
def edit_show(show_id):
    data = {
        'id': show_id
    }
    show = Show.get_show_by_id(data)
    show.release_date = str(show.release_date)[0:10]
    return render_template('show_edit.html', show = show)

# --------------------- Update --------------------


@app.route('/shows/<int:show_id>/update', methods=['POST'])
def update_show(show_id):
    if not Show.validate_new_show(request.form):
        return redirect(f"/shows/{show_id}/edit")

    else:
        data = {
        "name": request.form['show_name'],
        "network": request.form["network"],
        "release_date": request.form['release_date'],
        "description": request.form['description'],
        "id": show_id
    }
        Show.update_show(data)

        return redirect('/shows')


    # --------------- Delete -----------

@app.route('/shows/<int:show_id>/delete')
def delete_show(show_id):
    data = {
        'id': show_id
    }
    Show.delete_show(data)
    return redirect('/shows')