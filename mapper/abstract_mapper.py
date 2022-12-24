from abc import ABC, abstractmethod
from typing import Dict, Iterable, Generator

from domain.abstract_domain import AbstractDomain
from model.abstract import AbstractModel


class AbstractMapper(ABC):
    @abstractmethod
    def json_to_model(self, json: Dict) -> AbstractModel:
        pass

    def jsons_to_models(self, jsons: Iterable[Dict]) -> list[AbstractModel]:
        return [self.json_to_model(json) for json in jsons]

    @abstractmethod
    def model_to_json(self, model: AbstractModel) -> Dict:
        pass

    def models_to_jsons(self, models: Iterable[AbstractModel]) -> list[Dict]:
        return [self.model_to_json(model) for model in models]

    @abstractmethod
    def model_to_domain(self, model: AbstractModel) -> AbstractDomain:
        pass

    def models_to_domains(self, models: Iterable[AbstractModel]) -> list[AbstractDomain]:
        return [self.model_to_domain(model) for model in models]

    @abstractmethod
    def domain_to_model(self, model: AbstractDomain) -> AbstractModel:
        pass

    def domains_to_models(self, domains: Iterable[AbstractDomain]) -> list[AbstractDomain]:
        return [self.domain_to_model(domain) for domain in domains]
