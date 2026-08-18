from six_months.engine.state import GameState, TimeOfDay


def test_new_game_starts_on_day_one_morning() -> None:
    state = GameState()
    assert state.day == 1
    assert state.time_of_day is TimeOfDay.MORNING


def test_time_advances_through_day() -> None:
    state = GameState()

    state.advance_time()
    assert state.day == 1
    assert state.time_of_day is TimeOfDay.AFTERNOON

    state.advance_time()
    assert state.time_of_day is TimeOfDay.NIGHT

    state.advance_time()
    assert state.day == 2
    assert state.time_of_day is TimeOfDay.MORNING
