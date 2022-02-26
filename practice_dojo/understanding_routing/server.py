from flask import Flask

app = Flask(__name__) 

# -----------import controllers here--------------

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<word>')
def word(word):
    print(word)
    return "Hi, " + word

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output


if __name__ == '__main__':
    app.run(debug=True)