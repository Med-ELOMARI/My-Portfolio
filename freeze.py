# -*- encoding: utf-8 -*-

from flask_frozen import Freezer

from app import app

# ----------------------------------------
# launch
# ----------------------------------------

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()
