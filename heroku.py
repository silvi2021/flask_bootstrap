import os
from flask_migrate import upgrade
from app import create_app

app = create_app(os.getenv('ENVIRONMENT_CONFIG') or 'production')

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()