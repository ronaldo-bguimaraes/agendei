from typing import Dict

from domain.abstract_domain import AbstractDomain
from mapper.abstract_mapper import AbstractMapper
from model.abstract import RegionModel, AbstractModel


class RegionMapper(AbstractMapper):
    def json_to_model(self, json: Dict) -> RegionModel:
        return RegionModel(
            id_region=json['id'],
            postal=json['sigla'],
            name=json['nome'],
        )

    def model_to_json(self, model: RegionModel) -> Dict:
        return {
            'id': model.id_region,
            'sigla': model.postal,
            'nome': model.name,
        }

    def model_to_domain(self, model: RegionModel) -> AbstractDomain:
        pass

    def domain_to_model(self, model: AbstractDomain) -> AbstractModel:
        pass
