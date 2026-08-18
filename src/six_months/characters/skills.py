from dataclasses import dataclass


SKILL_NAMES = (
    "athletics",
    "melee",
    "firearms",
    "stealth",
    "survival",
    "scavenging",
    "first_aid",
    "navigation",
    "mechanics",
    "electronics",
    "persuasion",
    "intimidation",
    "deception",
    "leadership",
    "medicine",
    "investigation",
    "science",
)


@dataclass
class Skills:
    athletics: int = 0
    melee: int = 0
    firearms: int = 0
    stealth: int = 0
    survival: int = 0
    scavenging: int = 0
    first_aid: int = 0
    navigation: int = 0
    mechanics: int = 0
    electronics: int = 0
    persuasion: int = 0
    intimidation: int = 0
    deception: int = 0
    leadership: int = 0
    medicine: int = 0
    investigation: int = 0
    science: int = 0

    MAX_VALUE = 5

    def __post_init__(self) -> None:
        for name in SKILL_NAMES:
            value = getattr(self, name)
            if not isinstance(value, int) or not 0 <= value <= self.MAX_VALUE:
                raise ValueError(f"{name} must be an integer from 0 to {self.MAX_VALUE}")
