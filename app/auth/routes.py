from app.auth import bp
from flask import render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models.user import User

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users=users)



@bp.route('/register', methods =('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']        
        if not username:
            flash('El nombre de usuario es obligatorio')
        elif not email:
            flash('El correo es obligatorio') 
        elif not password == password_confirm:
            flash('La contraseña no coincide')   
        else:
            user = User(username = username, email = email, password_hash = password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.index'))                  
    return render_template('auth/register.html')

@bp.route('/<id>/update', methods = ('GET', 'POST'))
def update(id):
    message = Message.query.filter_by(id = id).first()
    if request.method == 'POST':
        if message:
            message.title = request.form['title']  
            message.content = request.form['content'] 
            message.picture = request.form['picture']
            db.session.commit() 
            return redirect('/')
    return render_template('messages/update.html', message = message)

@bp.route('/delete', methods = ['POST'])
def delete():
    id = request.form['id']
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Mensaje eliminado')
    return redirect('/')    