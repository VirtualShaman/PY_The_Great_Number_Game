from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='whatever'

@app.route('/')
def index():

    if 'result' not in session:
        session['result']=random.randint(1, 100)

    return render_template('index.html')

@app.route('/processing', methods=["POST"])
def numcheck():
    
    session['num']=int(request.form['num'])
    return redirect('/')

@app.route('/clear', methods=["GET"])
def clear():
    
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
