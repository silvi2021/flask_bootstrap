from flask import Flask, request, render_template, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] ="CUALQUIER COSA"

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages = messages)

@app.route('/create', methods =('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title:
            flash('El titulo es obligatorio')
        elif not content:
            flash('El contenido es obligatorio') 
        else:
            messages.append({'title': title, 'content': content}) 
            return redirect(url_for('index'))
                   
    return render_template('create.html')



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

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 400



