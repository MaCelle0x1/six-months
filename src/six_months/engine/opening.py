from six_months.engine.events import Choice, Event
from six_months.engine.state import GameState, TimeOfDay


def _advance(state: GameState, message: str) -> str:
    state.advance_time()
    return message


def opening_event(state: GameState) -> Event:
    def check_phone(game: GameState) -> str:
        return _advance(
            game,
            "Your phone is sitting on the nightstand. Three notifications are waiting. "
            "Two are ordinary. The third is from your local news station: "
            "'Officials investigating unusual illness at area hospital.'",
        )

    def look_outside(game: GameState) -> str:
        game.logistics += 0
        return "You pull the curtain aside. An ambulance is parked down the street. A neighbor is standing outside in a robe, watching it."

    def turn_on_tv(game: GameState) -> str:
        return _advance(
            game,
            "The morning news is mostly ordinary. Weather. Traffic. Then a brief local report: "
            "several patients were transported overnight after becoming suddenly disoriented. "
            "The reporter says officials have not identified a cause.",
        )

    def make_coffee(game: GameState) -> str:
        return _advance(game, "You make coffee. For the moment, the world still feels completely normal.")

    def stay_in_bed(game: GameState) -> str:
        game.advance_time()
        game.advance_time()
        return "You pull the blankets over your head and fall back asleep. When you wake again, it is afternoon."

    return Event(
        title="DAY 0 — MORNING",
        text=(
            "You wake to the sound of an ambulance outside.\n\n"
            "The siren has already stopped. You can hear voices somewhere down the street, "
            "but you can't make out what they're saying.\n\n"
            "Your alarm says 7:12 AM. Nothing else about the morning seems unusual."
        ),
        choices=(
            Choice("Check your phone", check_phone),
            Choice("Look out the window", look_outside),
            Choice("Turn on the television", turn_on_tv),
            Choice("Make coffee and start your morning", make_coffee),
            Choice("Go back to sleep", stay_in_bed),
        ),
    )
