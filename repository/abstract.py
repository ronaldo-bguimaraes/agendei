from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model.abstract import AbstractModel


class Database:
    def __init__(self):
        self._connection_string = 'mysql+pymysql://root:a77O0p9ZkgmDVfG@localhost:3306/base?charset=utf8mb4'
        self._engine = create_engine(self._connection_string)
        AbstractModel.metadata.create_all(self._engine)

    def session(self):
        return Session(self._engine)
