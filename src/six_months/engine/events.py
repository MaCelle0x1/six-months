import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from six_months.engine.state import GameState


@dataclass(frozen=True)
class Choice:
    id: str
    text: str
    effects: tuple[dict[str, Any], ...] = ()


@dataclass(frozen=True)
class Event:
    id: str
    title: str
    text: str
    choices: tuple[Choice, ...] = ()


LORE = {
    "local_news_01": "Your phone is sitting on the nightstand. Three notifications are waiting. Two are ordinary. The third is from your local news station: 'Officials investigating unusual illness at area hospital.'",
    "ambulance_outside": "You pull the curtain aside. An ambulance is parked down the street. A neighbor is standing outside in a robe, watching it.",
    "local_news_02": "The morning news is mostly ordinary. Weather. Traffic. Then a brief local report: several patients were transported overnight after becoming suddenly disoriented. The reporter says officials have not identified a cause."
}


class EffectEngine:
    """Interprets generic effects declared by narrative content."""

    def __init__(self, state: GameState) -> None:
        self.state = state

    def apply(self, effect: dict[str, Any]) -> str | None:
        effect_type = effect["type"]

        if effect_type == "advance_time":
            for _ in range(effect.get("segments", 1)):
                self.state.advance_time()
            return None

        if effect_type == "reveal_lore":
            try:
                return LORE[effect["id"]]
            except KeyError as exc:
                raise ValueError(f"Unknown lore id: {effect['id']}") from exc

        if effect_type == "set_flag":
            self.state.flags.add(effect["id"])
            return None

        raise ValueError(f"Unknown effect type: {effect_type}")


class EventEngine:
    """Presents events loaded from content and applies their declared effects."""

    def __init__(self, state: GameState) -> None:
        self.state = state
        self.effects = EffectEngine(state)

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
                choice = event.choices[int(raw) - 1]
            except (ValueError, IndexError):
                print("Please choose one of the listed options.")
                continue

            for effect in choice.effects:
                message = self.effects.apply(effect)
                if message:
                    print(f"\n{message}")
            return


def load_event(path: str | Path) -> Event:
    """Load a narrative event from a JSON content file."""
    with Path(path).open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Event(
        id=data["id"],
        title=data["title"],
        text=data["text"],
        choices=tuple(
            Choice(
                id=choice["id"],
                text=choice["text"],
                effects=tuple(choice.get("effects", [])),
            )
            for choice in data["choices"]
        ),
    )
