from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrecy is key'


@app.route('/')
def index():
    if 'user_count' not in session:
        session['user_count'] = 0
    session['user_count'] += 1
    print(session['user_count'])
    return render_template('index.html', user_count = session['user_count'])
    # return redirect ('/')???
    # needs to redrect to the original route

@app.route('/destroy_session')
def reset():
    session.pop('user_count')
    return redirect('/')

    # add two to the count
@app.route('/add_two_button', methods=['POST'])
def add_two():
    session['user_count'] += 1
    print(session['user_count'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

