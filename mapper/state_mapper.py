from typing import Dict

from mapper.abstract_mapper import AbstractMapper
from mapper.region_mapper import RegionMapper
from model.abstract import StateModel


class StateMapper(AbstractMapper):
    @staticmethod
    def json_to_model(json: Dict):
        return StateModel(
            id_state=json['id'],
            postal=json['sigla'],
            name=json['nome'],
            region=RegionMapper.json_to_model(**json['regiao'])
        )
