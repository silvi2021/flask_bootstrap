from flask import Blueprint

bp = Blueprint('memes', __name__)

from app.memes import routes
