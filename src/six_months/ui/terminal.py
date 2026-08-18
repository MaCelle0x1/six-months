from pathlib import Path

from six_months.characters.creator import create_character
from six_months.engine.events import EventEngine, load_event
from six_months.engine.game import Game


CONTENT_ROOT = Path(__file__).resolve().parents[3] / "content"


def show_state(game: Game) -> None:
    state = game.state
    print("\n" + "=" * 52)
    print(f"DAY {state.day} — {state.time_of_day.value.upper()}")
    print("=" * 52)
    print(f"Logistics: {state.logistics}")
    print()


def run_terminal(game: Game) -> None:
    print("SIX MONTHS")
    print("A grounded survival RPG")
    print()

    game.state.player = create_character()
    print(f"\nYou are {game.state.player.describe()}.")
    print()
    input("Press Enter to begin...")

    opening_path = CONTENT_ROOT / "events" / "day_0_wake_up.json"
    opening = load_event(opening_path)
    EventEngine(game.state).present(opening)

    while game.state.running:
        show_state(game)
        print(f"You are {game.state.player.describe()}.")
        print()
        print("1. Continue")
        print("2. End game")
        choice = input("> ").strip()

        if choice == "1":
            game.advance()
        elif choice == "2":
            game.state.running = False
        else:
            print("Please choose 1 or 2.")

    print("\nGame over.")
