from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_user():
    return "Hello, and Welcome"

@app.route('/play/')
def play():
    return render_template("index.html")

@app.route('/play/<int:x>')
def play_x(x):
    return render_template("index.html", x = x)


# @app.route('/play/(x)/(color)')
# def play_x_color(x, color):
#     return render_template("index.html", x = x, color = color)









if __name__=="__main__":   
    app.run(debug=True)  
