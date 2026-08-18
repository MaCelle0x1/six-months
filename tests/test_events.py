from pathlib import Path

from six_months.engine.events import EventEngine, load_event
from six_months.engine.state import GameState, TimeOfDay


OPENING = Path(__file__).parents[1] / "content" / "events" / "day_0_wake_up.json"


def test_new_game_begins_on_day_zero() -> None:
    state = GameState()
    assert state.day == 0
    assert state.time_of_day is TimeOfDay.MORNING


def test_opening_event_is_loaded_from_json() -> None:
    event = load_event(OPENING)
    assert event.id == "day_0_wake_up"
    assert event.title == "DAY 0 — MORNING"
    assert len(event.choices) == 5
    assert event.choices[0].id == "check_phone"


def test_phone_choice_advances_time_reveals_lore_and_adds_phone() -> None:
    state = GameState()
    event = load_event(OPENING)
    engine = EventEngine(state)

    messages = [engine.effects.apply(effect) for effect in event.choices[0].effects]

    assert state.time_of_day is TimeOfDay.AFTERNOON
    assert state.inventory.has("phone")
    assert any(message and "unusual illness" in message for message in messages)


def test_make_coffee_can_add_a_mundane_item() -> None:
    state = GameState()
    event = load_event(OPENING)
    engine = EventEngine(state)

    for effect in event.choices[3].effects:
        engine.effects.apply(effect)

    assert state.inventory.has("rubber_band")
    assert state.time_of_day is TimeOfDay.AFTERNOON


def test_json_choice_can_set_a_flag() -> None:
    state = GameState()
    event = load_event(OPENING)
    engine = EventEngine(state)

    for effect in event.choices[4].effects:
        engine.effects.apply(effect)

    assert "slept_through_morning" in state.flags
    assert state.time_of_day is TimeOfDay.NIGHT
