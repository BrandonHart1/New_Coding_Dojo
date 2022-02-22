from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<id>')
def say(id):
    return f"Hi {id}!"

@app.route('/repeat/<id_num>/<id_word>')
def repeat(id_num, id_word):
    output = ""
    for i in range(0, int(id_num)):
        output += f"<h1>{id_word}</h1>"
    return output

if __name__=="__main__":   
    app.run(debug=True)  



