from dataclasses import dataclass
from typing import Protocol


@dataclass
class Loader(Protocol):
    def get_yearly_salary(self) -> list[tuple[str, str]]:
        raise NotImplementedError(
            "Please implement get_yearly_salary in the child class."
        )
