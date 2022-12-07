from app.main import bp
from flask import render_template


@bp.route('/')
def index():
    return render_template('index.html')

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404
