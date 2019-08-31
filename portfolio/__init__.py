from flask import Flask

from portfolio.app.data import Data
from portfolio.app.views import portfolio_blueprint
from portfolio.blog.views import blog_blueprint

app = Flask(__name__, static_url_path='')

# Configuration of application, see configuration.py, choose one and uncomment.
# app.config.from_object('app.configuration.ProductionConfig')
app.config.from_object('portfolio.configuration.DevelopmentConfig')
app.register_blueprint(portfolio_blueprint)
app.register_blueprint(blog_blueprint)

# Expose globals to Jinja2 templates
app.add_template_global(app.config, 'cfg')
app.add_template_global(Data, 'data')
