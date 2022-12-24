from typing import Iterable

from model.abstract import UserModel
from repository.abstract import Database


class UserRepository:
    def __init__(self):
        self._db = Database()

    def save(self, user_list: Iterable[UserModel]):
        with self._db.session() as session:
            session.add_all(user_list)
            session.commit()

    def all(self) -> Iterable[UserModel]:
        with self._db.session() as session:
            return session.query(UserModel).all()

    def find(self, email: str) -> UserModel:
        with self._db.session() as session:
            return session.query(UserModel).where(UserModel.email == email).one()
