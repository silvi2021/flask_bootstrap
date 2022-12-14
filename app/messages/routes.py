from flask import render_template, request, flash, redirect, url_for
from app.messages import bp 
from app.extensions import db
from app.models.message import Message
from flask_login import login_required, current_user




@bp.route('/')
@login_required
def index():
    messages = Message.query.filter_by(user = current_user)
    return render_template('messages/index.html', messages = messages)

@bp.route('/create', methods =('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        picture = request.form['picture'] 
        price = request.form['price']
        link = request.form['link']  
             
        if not title:
            flash('El titulo es obligatorio')
        elif not content:
            flash('El contenido es obligatorio') 
        else:
            message = Message(title = title, content = content, picture = picture, user = current_user, price = price, link = link)
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('messages.index'))                  
    return render_template('messages/create.html')

@bp.route('/<id>/update', methods = ('GET', 'POST'))
@login_required
def update(id):
    message = Message.query.filter_by(id = id).first()
    if request.method == 'POST':
        if message:
            message.title = request.form['title']  
            message.content = request.form['content'] 
            message.picture = request.form['picture']
            message.price = request.form['price']
            message.link = request.form['link']
            print(request.form['price'])
            print(request.form['link'])
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
    
