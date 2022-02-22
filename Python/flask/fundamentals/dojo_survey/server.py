from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrecy is key'

# ------------------  index route  -----------------
@app.route('/')
def index():
    return render_template('/index.html')

# ---------------  process information  ------------------
@app.route('/process', methods=['POST']) # post route
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect ('/result')

    
# ---------------  route for results page  ------------------
@app.route('/result')
def result():
    return render_template('result.html')

# ---------**********  save form data into session  **********--------




if __name__ == "__main__":
    app.run(debug=True)