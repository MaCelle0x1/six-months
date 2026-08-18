from dataclasses import dataclass, field

from .attributes import Attributes
from .skills import Skills


@dataclass
class Character:
    name: str
    age: int
    occupation: str
    background: str
    attributes: Attributes = field(default_factory=Attributes)
    skills: Skills = field(default_factory=Skills)

    def describe(self) -> str:
        return f"{self.name}, {self.age} — {self.occupation}"
