from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self, param):
        response = {
            "status": "ok",
            "param": param
        }
        return response, 200

api.add_resource(User, "/test/<string:param>")

app.run(host='0.0.0.0', debug=True)
