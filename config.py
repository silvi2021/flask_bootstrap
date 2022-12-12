import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''Clase base para asignar las constantes de configuración desde variables de entorno.
       Las constantes aquí declaradas aplican para todos los entornos'''
    FLASK_APP='app'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    '''Clase para el entorno de desarrollo'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    '''Clase para el entorno de pruebas'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'+ os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    '''Clase para el entorno de producción'''
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = uri


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}














