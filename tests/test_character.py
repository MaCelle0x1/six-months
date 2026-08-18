import pytest

from six_months.characters.attributes import Attributes
from six_months.characters.character import Character
from six_months.characters.skills import Skills


def test_character_stores_identity_and_background() -> None:
    character = Character(
        name="Alex",
        age=27,
        occupation="Paramedic",
        background="Worked night shifts and lived alone.",
    )

    assert character.name == "Alex"
    assert character.age == 27
    assert character.occupation == "Paramedic"
    assert character.background.startswith("Worked")


def test_attributes_reject_invalid_values() -> None:
    with pytest.raises(ValueError):
        Attributes(might=11)


def test_skills_reject_invalid_values() -> None:
    with pytest.raises(ValueError):
        Skills(firearms=6)
