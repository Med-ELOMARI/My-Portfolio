# -*- encoding: utf-8 -*-

import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


# Only cfg is here ..
class AppConfig(object):
    THEME = 'phantom'

    STATIC = 'static'
    DATE_FORMAT = '%Y-%m-%d'


class Config(AppConfig):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False
    BOOTSTRAP_FONTAWESOME = True
    CSRF_ENABLED = True


class ProductionConfig(Config):
    APP = 'PATH_FOR_PRODUCTION'
    APP_IMG_FOLDER = os.path.join(APP, 'static', 'images')

    # RECAPTCHA keys (production)
    RECAPTCHA_PUBLIC_KEY = "1234_abcd"
    RECAPTCHA_PRIVATE_KEY = "1234_xyzw"

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    APP = 'app'
    APP_IMG_FOLDER = os.path.join(APP, 'static', 'images')

    # keys for dev [ http://localhost ]
    RECAPTCHA_PUBLIC_KEY = "1234_abcd"
    RECAPTCHA_PRIVATE_KEY = "1234_xyzw"

    DEBUG = False
    TESTING = False
    FORCE_HTTPS = False
