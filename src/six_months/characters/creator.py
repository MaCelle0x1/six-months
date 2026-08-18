from .attributes import Attributes
from .character import Character
from .skills import Skills


def _ask(prompt: str, default: str | None = None) -> str:
    while True:
        suffix = f" [{default}]" if default is not None else ""
        value = input(f"{prompt}{suffix}: ").strip()
        if value:
            return value
        if default is not None:
            return default
        print("Please enter a value.")


def _ask_int(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        raw = input(f"{prompt} ({minimum}-{maximum}): ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Please choose a number from {minimum} to {maximum}.")


def create_character() -> Character:
    print("\nCHARACTER CREATION")
    print("=" * 52)

    name = _ask("Name")
    age = _ask_int("Age", 16, 90)
    occupation = _ask("Occupation", "Unemployed")
    background = _ask("Brief background", "Ordinary life")

    print("\nFor now, attributes use a simple 1–10 scale.")
    print("These defaults will be replaced by a proper point-buy system later.\n")

    attributes = Attributes(
        might=_ask_int("Might", 1, 10),
        agility=_ask_int("Agility", 1, 10),
        vitality=_ask_int("Vitality", 1, 10),
        intellect=_ask_int("Intellect", 1, 10),
        awareness=_ask_int("Awareness", 1, 10),
        presence=_ask_int("Presence", 1, 10),
    )

    return Character(
        name=name,
        age=age,
        occupation=occupation,
        background=background,
        attributes=attributes,
        skills=Skills(),
    )
