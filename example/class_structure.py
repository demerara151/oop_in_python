"""
Example of OOP in python.

Keywords:
    Abstract: 抽象的な、ぼんやりした
    Inheritance: 継承、受け継ぐ、引き継ぐ
    Composition: 合成、（複数のものからひとつに）形を成す
"""
from dataclasses import dataclass
from typing import Protocol


# Abstract class
class Language(Protocol):
    "Parent class"

    def say_hello(self) -> None:
        raise NotImplementedError


# Concrete class
class French(Language):
    "Child class  of Language class"

    def say_hello(self) -> None:
        print("Bonjour")


# Concrete class
class Japanese(Language):
    "Child class of Language class"

    def say_hello(self) -> None:
        print("こんちにわ")


# Inherit from Abstract class is good.
# Inherit from Concrete class is bad.
# Using Composition instead of Inheritance from Concrete class.


# Another Concrete class
@dataclass(slots=True, frozen=True)
class Speaker:
    "Using Composition instead of Inheritance."
    language: Language  # Any languages under the Language class.

    def speak(self) -> None:
        self.language.say_hello()


if __name__ == "__main__":
    jp = Japanese()
    speaker = Speaker(language=jp)
    speaker.speak()

    fr = French()
    speaker = Speaker(language=fr)
    speaker.speak()
