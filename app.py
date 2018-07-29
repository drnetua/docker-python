from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class TestController(Resource):
    def get(self, param):
        response = {
            "status": "ok",
            "param": param
        }
        return response, 200

class QuitController(Resource):
    def get(self):
        shutdown_server()
        return 'Server shutting down...'

api.add_resource(TestController, "/test/<string:param>")
api.add_resource(QuitController, "/quit")

app.run(host='0.0.0.0', debug=True)
