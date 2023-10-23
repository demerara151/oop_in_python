from dataclasses import dataclass

from loader import CSVLoader, JSONLoader, Loader
from src.writer import Writer


@dataclass
class Employee:
    loader: Loader
    writer: Writer

    def write(self) -> None:
        database = self.loader.get_yearly_salary()
        self.writer.write_salary(database)


if __name__ == "__main__":
    writer = Writer()

    csv_loader = CSVLoader()
    employee = Employee(csv_loader, writer)
    employee.write()

    json_loader = JSONLoader()
    employee = Employee(json_loader, writer)
    employee.write()
