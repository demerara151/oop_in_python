# type: ignore
# flake8: noqa
from dataclasses import dataclass
from typing import Protocol

from loader.csv import CSVLoader
from loader.json import JSONLoader


@dataclass
class Loader(Protocol):
    def get_yearly_salary(self) -> list[tuple[str, str]]:
        raise NotImplementedError(
            "Please implement get_yearly_salary in the child class."
        )
