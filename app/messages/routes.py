from flask import render_template, request, flash, redirect, url_for
from app.messages import bp 
from app.extensions import db
from app.models.message import Message

@bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('messages/index.html', messages = messages)

@bp.route('/create', methods =('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        picture = request.form['picture']        
        if not title:
            flash('El titulo es obligatorio')
        elif not content:
            flash('El contenido es obligatorio') 
        else:
            message = Message(title = title, content = content, picture = picture)
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('messages.index'))                  
    return render_template('messages/create.html')

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
    
