"Polymorphism"
from typing import Protocol


# Abstract class
class Language(Protocol):
    "Parent class"

    def say_hello(self) -> None:
        raise NotImplementedError


# Concrete class
class French(Language):
    "Child class of Language class"

    def say_hello(self) -> None:
        print("Bonjour")


# Concrete class
class Japanese(Language):
    "Child class of Language class"

    def say_hello(self) -> None:
        print("こんちにわ")


if __name__ == "__main__":
    # Polymorphism
    fr = French()
    jp = Japanese()
    for lang in [fr, jp]:
        lang.say_hello()
    """
    別のクラスでも同じメッソド名で処理を呼び出せる
    これをポリモーフィズム（多態性）という

    ポリモーフィズムの実現のためには、親クラスからの継承が必要になる
    しかし、継承では融通が効かないことが多々あるため、継承元の親クラスを融通の効く抽象クラスとする

    抽象クラスでは、メソッドの署名部分のみを定義し、実際の内容は記述しない
    引数と戻り値の型は、抽象クラスで定義されたものに従う必要がある
    """
