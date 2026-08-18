from dataclasses import dataclass, field
from typing import Callable

from six_months.engine.state import GameState


@dataclass(frozen=True)
class Choice:
    text: str
    action: Callable[[GameState], str]


@dataclass(frozen=True)
class Event:
    title: str
    text: str
    choices: tuple[Choice, ...] = field(default_factory=tuple)


class EventEngine:
    """Presents narrative events and applies their choice effects."""

    def __init__(self, state: GameState) -> None:
        self.state = state

    def present(self, event: Event) -> None:
        print(f"\n{event.title}")
        print("-" * len(event.title))
        print(event.text)
        print()

        for index, choice in enumerate(event.choices, start=1):
            print(f"{index}. {choice.text}")

        while True:
            raw = input("> ").strip()
            try:
                selected = int(raw) - 1
                choice = event.choices[selected]
            except (ValueError, IndexError):
                print("Please choose one of the listed options.")
                continue
            result = choice.action(self.state)
            if result:
                print(f"\n{result}")
            break
