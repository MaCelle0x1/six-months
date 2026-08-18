from dataclasses import dataclass


@dataclass
class Attributes:
    might: int = 5
    agility: int = 5
    vitality: int = 5
    intellect: int = 5
    awareness: int = 5
    presence: int = 5

    MIN_VALUE = 1
    MAX_VALUE = 10

    def __post_init__(self) -> None:
        values = vars(self)
        for name, value in values.items():
            if not isinstance(value, int) or not self.MIN_VALUE <= value <= self.MAX_VALUE:
                raise ValueError(f"{name} must be an integer from {self.MIN_VALUE} to {self.MAX_VALUE}")
