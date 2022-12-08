from app.main import bp
from flask import render_template
from app.models.message import Message


@bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages = messages)

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404
