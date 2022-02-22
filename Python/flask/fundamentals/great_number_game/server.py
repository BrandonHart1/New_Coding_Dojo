from flask import Flask, render_template, redirect, request, session
import random
app= Flask(__name__)
app.secret_key = '824824824'

@app.route('/')
def index():
    session['computer_num'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/process_guess')
def process_guess():
    print('**********')
    print(f"User guessed: {request.form['guess']}")
    user_guess = int(request.form['guess'])
    computer_num = int(request.form['computer_num'])
    if (user_guess > computer_num):
        is_too_high = True
        print('Too High')
    elif (user_guess < computer_num):
        is_too_low = True
        print('Sorry. Too low.')
    else:
        is_correct = True
        print("You're a LEGEND")
    return redirect('/results')

@app.route('/results')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)