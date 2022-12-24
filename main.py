from flask import Flask
from flask_restful import Api

from controller.user_controller import UserController

app = Flask(__name__)

api = Api(app)

api.add_resource(
    resource=UserController,
    urls='/user',
    endpoint='get',
    methods=['GET'],
)

api.add_resource(
    resource=UserController,
    urls='/user/login',
    endpoint='login',
    methods=['POST'],
)

if __name__ == '__main__':
    app.run(debug=True)
