# -*- encoding: utf-8 -*-

import os

from portfolio import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)
    # app.run(ssl_context='adhoc')
