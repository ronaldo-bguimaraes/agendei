from typing import Iterable

from domain.user_domain import UserDomain
from mapper.user_mapper import UserMapper
from repository.user import UserRepository


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()
        self._user_mapper = UserMapper()

    def all(self):
        return (self._user_mapper.model_to_domain(user) for user in self._user_repository.all())

    def add(self, users: Iterable[UserDomain]):
        domain_users = (self._user_mapper.domain_to_model(user) for user in users)
        self._user_repository.save(domain_users)

    def find(self, email: str) -> UserDomain:
        user_model = self._user_repository.find(email)
        return self._user_mapper.model_to_domain(user_model)
