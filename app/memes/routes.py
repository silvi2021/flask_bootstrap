from app.memes import bp
from flask import render_template


@bp.route('/')
def index():
    return render_template('memes/index.html')