from dataclasses import dataclass, field
from enum import Enum


class TimeOfDay(str, Enum):
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    NIGHT = "Night"


@dataclass
class GameState:
    day: int = 1
    time_of_day: TimeOfDay = TimeOfDay.MORNING
    running: bool = True
    player_name: str | None = None
    logistics: int = 100

    def advance_time(self) -> None:
        if self.time_of_day is TimeOfDay.MORNING:
            self.time_of_day = TimeOfDay.AFTERNOON
        elif self.time_of_day is TimeOfDay.AFTERNOON:
            self.time_of_day = TimeOfDay.NIGHT
        else:
            self.day += 1
            self.time_of_day = TimeOfDay.MORNING
