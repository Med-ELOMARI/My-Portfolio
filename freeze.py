# -*- encoding: utf-8 -*-

from flask_frozen import Freezer

from portfolio import app

freezer = Freezer(app)


@freezer.register_generator
def index():
    # fixed the index not found by the freezer
    yield "portfolio_blueprint.index", {}
    yield "blog_blueprint.index", {}


if __name__ == "__main__":
    for i in freezer.freeze_yield():
        print(i)
    # freezer.freeze()
