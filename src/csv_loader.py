import csv
from dataclasses import dataclass

from src.protocol import Loader


@dataclass
class CSVLoader(Loader):
    def get_yearly_salary(self) -> list[tuple[str, str]]:
        with open("csv/employee.csv", "r") as f:
            csv_data = csv.reader(f)
            _ = next(csv_data)
            return [(name, value) for name, value in csv_data]
