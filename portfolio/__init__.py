from flask import Flask

from portfolio.blog.views import blog_blueprint
from portfolio.data import Data
from portfolio.intro.views import portfolio_blueprint

app = Flask(__name__, static_url_path='')

# Configuration of application, see configuration.py, choose one and uncomment.
# intro.config.from_object('intro.configuration.ProductionConfig')
app.config.from_object('portfolio.configuration.DevelopmentConfig')
print(portfolio_blueprint.static_folder)
print(blog_blueprint.static_folder)
app.register_blueprint(portfolio_blueprint)
app.register_blueprint(blog_blueprint)

# Expose globals to Jinja2 templates
app.add_template_global(app.config, 'cfg')
app.add_template_global(Data, 'data')
