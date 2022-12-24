from typing import Dict

from sqlalchemy import Column, Integer, String, Date, CHAR, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

AbstractModel = declarative_base()


class UserModel(AbstractModel):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(45))
    birth_date = Column(Date)
    email = Column(String(45))
    password = Column(String(32))
    addresses = relationship('Address', back_populates='user')
    customers = relationship('Customer', back_populates='user')
    providers = relationship('Provider', back_populates='user')


class AddressModel(AbstractModel):
    __tablename__ = 'address'
    id_address = Column(Integer, primary_key=True)
    street = Column(String(50))
    neighborhood = Column(String(50))
    city = Column(String(50))
    postal_code = Column(CHAR(8))
    main = Column(Boolean)
    id_user = Column(Integer, ForeignKey("user.id_user"))
    user = relationship("User", back_populates="addresses")


class CustomerModel(AbstractModel):
    __tablename__ = 'customer'
    id_customer = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id_user"))
    user = relationship("User", back_populates="customers")


class ProviderModel(AbstractModel):
    __tablename__ = 'provider'
    id_customer = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id_user"))
    user = relationship("User", back_populates="providers")


class RegionModel:
    def __init__(self, id_region: str, postal: str, name: str):
        self.id_region = id_region
        self.postal = postal
        self.name = name

    @staticmethod
    def from_json(json: Dict):
        return RegionModel(
            id_region=json['id'],
            postal=json['sigla'],
            name=json['nome']
        )


class StateModel:
    def __init__(self, id_state, postal, name, region):
        self.id_state = id_state
        self.postal = postal
        self.state = name
        self.region = RegionModel(**region)

    @staticmethod
    def from_json(json: Dict):
        return StateModel(
            id_state=json['id'],
            postal=json['sigla'],
            name=json['nome'],
            region=RegionModel.from_json(json['regiao'])
        )
