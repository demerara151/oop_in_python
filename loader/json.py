import json
from dataclasses import dataclass

from loader import Loader


@dataclass
class JSONLoader(Loader):
    def get_yearly_salary(self) -> list[tuple[str, str]]:
        with open("json/employee.json", "rb") as f:
            data = json.load(f)

        return [
            (record["name"], record["salary"]) for record in data["employee"]
        ]
