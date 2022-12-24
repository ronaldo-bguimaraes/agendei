from flask import request
from flask_restful import Resource

from service.user_service import UserService


class UserController(Resource):
    def __init__(self):
        self.user_service = UserService()
        pass

    def get(self):
        return {'hello': 'world'}

    def login(self):
        email = request.form['email']
        user_domain = self.user_service.find(email)
        print(user_domain)
