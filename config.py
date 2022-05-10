import os

class Config:
    '''General configuration parent class'''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:bioactive@localhost/pitchme'

    # Replace the username with user we created when configuring PostgreSQL and password with the user's password.

class ProdConfig(Config):
    '''Production configuration child class
    Args: 
        Config: The parent configuration class with General configuration settings'''

    pass

class DevConfig(Config):
    '''Development configuration child class
    Args: 
        Config: The parent configuration class with General configuration settings'''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
    