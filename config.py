import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/data_eng_live"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/data_eng_dev"


class TestingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/data_eng_test"
