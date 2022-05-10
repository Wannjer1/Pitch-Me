from ensurepip import bootstrap
from flask import Flask 
from flask bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)