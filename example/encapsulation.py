"Encapsulation"
import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True, frozen=True)
class EnvVar:
    """
    メンバー名の先頭にアンダースコアを付けることで、クラスの外で呼び出すことを制限できる
    しかしながら、実際は呼び出すことができてしまうので注意が必要
    """

    @property
    def _api_key(self) -> str | None:
        load_dotenv()
        return os.getenv("API")

    def get_api_key(self) -> None:
        # Property is set when property decorated function runs.
        print(self._api_key)


if __name__ == "__main__":
    ev = EnvVar()
    # Instance of EnvVar() is an empty object at here.
    print(ev)

    """
    The property `_api_key` is protected,
    and cannot use it outside of the class.
    """
    # print(ev._api_key)

    # api_key is initialized here and pass it to the function
    ev.get_api_key()

    """
    However, EnvVar() instance is still an empty object.
    It doesn't contain `_api_key` parameter as an object.
    """
    print(ev)
