# -*- encoding: utf-8 -*-

from flask_frozen import Freezer

from app import app

freezer = Freezer(app)


@freezer.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield 'index', {}


if __name__ == "__main__":

    for i in freezer.freeze_yield():
        print(i)
    freezer.freeze()
