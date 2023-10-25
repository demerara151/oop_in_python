"Composition"
from dataclasses import dataclass

from .polymorphism import French, Japanese, Language


# Another Concrete class
@dataclass(slots=True, frozen=True)
class Speaker:
    "Using Composition instead of Inheritance."
    language: Language  # Any languages under the Language class.

    def speak(self) -> None:
        self.language.say_hello()  # `self.say_hello()` if inherit


if __name__ == "__main__":
    jp = Japanese()
    french_speaker = Speaker(language=jp)
    french_speaker.speak()

    fr = French()
    japanese_speaker = Speaker(language=fr)
    japanese_speaker.speak()
