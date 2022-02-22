from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def board():
    return render_template('index.html')

# for i in 

if __name__=="__main__":   
    app.run(debug=True)  

