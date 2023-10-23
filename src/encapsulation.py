"""Encapsulation example"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True, frozen=True)
class EnvVar:
    @property
    def api_key(self) -> str | None:
        load_dotenv()
        return os.getenv("API")


if __name__ == "__main__":
    ev = EnvVar()
    # Instance of EnvVar() is an empty object at here.
    print(ev)

    # Property is set when property decorated function runs.
    api_key = ev.api_key
    print(api_key)

    # However, EnvVar() instance is still an empty object.
    # It doesn't contain `api_key` parameter as an object.
    print(ev)
