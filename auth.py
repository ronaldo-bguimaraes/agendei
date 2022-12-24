from flask_httpauth import HTTPTokenAuth

from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPTokenAuth(scheme='Bearer')

tokens = []


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


@auth.error_handler
def auth_error():
    return "Access Denied", 403  # this is flask-restful return 403


JSONWebSignatureSerializer