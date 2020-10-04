from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import os


def create_app(config_type="dev"):
    if config_type == "dev":
        configuration = DevelopmentConfig
        print("Using development config")
    elif config_type == "test":
        configuration = TestingConfig
        print("Using testing config")
    elif config_type == "prod":
        configuration = ProductionConfig
        print("Using production config")
    else:
        raise ValueError("Invalid config type:", config_type)

    app = Flask(__name__)
    app.config.from_object(configuration)
    db = SQLAlchemy(app)

    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command("db", MigrateCommand)

    ma = Marshmallow(app)

    api = Api(app)

    return app, manager, ma, api, db


config_type_ = os.environ["CONFIG_TYPE"]
app, manager, ma, api, db = create_app(config_type=config_type_)


@app.route("/")
def test():
    return "test"


@app.route("/greet")
def say_hello():
    return "Hello from Server"


if __name__ == "__main__":
    manager.run()
