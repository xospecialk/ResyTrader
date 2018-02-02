from flask_restful import Resource
from flask_restful import reqparse


class Available(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):

        from trader import get_connection
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("Select 1111")
        rows = cursor.fetchall()
        return rows
