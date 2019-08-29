# -*- encoding: utf-8 -*-

from flask import Flask

# load RES
from .data import Data

app = Flask(__name__, static_url_path='/static')

# Configuration of application, see configuration.py, choose one and uncomment.
# app.config.from_object('app.configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')

# Expose globals to Jinja2 templates
app.add_template_global(app.config, 'cfg')
app.add_template_global(Data, 'data')

from app import views
