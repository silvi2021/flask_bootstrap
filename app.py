from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/usuario/<name>')
def user(name):
    return render_template('user.html', name = name)


@app.route('/usuario')
def user_incognito():
    return render_template('user.html')    


@app.route('/navegador')
def browser():
    user_agent = request.headers.get('User_Agent')
    return f'Tu navegador es:{user_agent}'


@app.route('/rutas')
def routes():
    print(app.url_map)
    return 'Revisa tu consola para ver las rutas'



