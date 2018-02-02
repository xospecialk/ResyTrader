from flask import Flask
from flask_restful import Api

from trader.utils.db_connection import create_new_connection
from trader.v1.availability import Available

db = None


def get_connection():

    return db


def create_app():

    global db
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Available,"/v1/available/", endpoint="api.trader.v1.availability")

    db = create_new_connection()
    return app


