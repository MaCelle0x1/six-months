from six_months.engine.events import EventEngine
from six_months.engine.opening import opening_event
from six_months.engine.state import GameState, TimeOfDay


def test_new_game_begins_on_day_zero() -> None:
    state = GameState()
    assert state.day == 0
    assert state.time_of_day is TimeOfDay.MORNING


def test_opening_event_has_five_choices() -> None:
    state = GameState()
    event = opening_event(state)
    assert event.title == "DAY 0 — MORNING"
    assert len(event.choices) == 5


def test_look_outside_does_not_advance_time() -> None:
    state = GameState()
    event = opening_event(state)
    event.choices[1].action(state)
    assert state.day == 0
    assert state.time_of_day is TimeOfDay.MORNING


def test_checking_phone_advances_to_afternoon() -> None:
    state = GameState()
    event = opening_event(state)
    event.choices[0].action(state)
    assert state.time_of_day is TimeOfDay.AFTERNOON


def test_going_back_to_sleep_advances_to_afternoon() -> None:
    state = GameState()
    event = opening_event(state)
    event.choices[4].action(state)
    assert state.day == 0
    assert state.time_of_day is TimeOfDay.NIGHT
