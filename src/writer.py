from dataclasses import dataclass


@dataclass
class Writer:
    def write_salary(self, db: list[tuple[str, str]]) -> None:
        for name, value in db:
            with open(name, "w") as f:
                salary = int(value) * 12
                f.write(str(object=salary))
