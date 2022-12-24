from typing import Dict

from domain.abstract_domain import AbstractDomain
from domain.user_domain import UserDomain
from mapper.abstract_mapper import AbstractMapper
from model.abstract import UserModel, AbstractModel


class UserMapper(AbstractMapper):

    def json_to_model(self, json: Dict) -> UserModel:
        return UserModel(
            id_user=json['id_user'],
            first_name=json['first_name'],
            last_name=json['model.last_name'],
            birth_date=json['birth_date'],
            email=json['email'],
            password=json['password'],
        )

    def model_to_json(self, model: UserModel) -> Dict:
        return {
            'id_user': model.id_user,
            'first_name': model.first_name,
            'last_name': model.last_name,
            'birth_date': model.birth_date,
            'email': model.email,
            'password': model.password,
        }

    def model_to_domain(self, model: UserModel) -> UserDomain:
        return UserDomain(
            id_user=model.id_user,
            first_name=model.first_name,
            last_name=model.last_name,
            birth_date=model.birth_date,
            email=model.email,
            password=model.password,
        )

    def domain_to_model(self, domain: UserDomain) -> UserModel:
        return UserModel(
            id_user=domain.id_user,
            first_name=domain.first_name,
            last_name=domain.last_name,
            birth_date=domain.birth_date,
            email=domain.email,
            password=domain.password,
        )
