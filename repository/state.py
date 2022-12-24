import requests

from model.abstract import StateModel


class StateRepository:
    def __init__(self):
        self.base_url = 'http://servicodados.ibge.gov.br/api/v1/localidades/estados'

    def all(self):
        return (StateModel.from_json(**state) for state in requests.get(self.base_url).json())
