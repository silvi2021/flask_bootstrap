from app.auth import bp
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user
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
            user = User(username = username, email = email, password = password)
            db.session.add(user)
            db.session.commit()
            flash('usuario creado correctamente')
            return redirect(url_for('auth.index'))                  
    return render_template('auth/register.html')

@bp.route('/login', methods =('GET', 'POST'))
def login():
    if request.method == 'POST':     
        email = request.form['email']
        password = request.form['password'] 
        remember = request.form.get('remember_me')         
        if not password:
            flash('La contraseña de usuario es obligatorio')
        elif not email:
            flash('El correo es obligatorio') 
        else:
            user = User.query.filter_by(email=email).first()
            if user and user.verify_password(password):
                login_user(user, remember) 
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                flash(f'Bienvenido {user.username}')
                return redirect(next)
            flash('usuario o password incorrecto')                            
    return render_template('auth/login.html')


@bp.route('logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect('/auth/login')
  

