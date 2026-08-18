from six_months.characters.creator import create_character
from six_months.engine.game import Game


def show_state(game: Game) -> None:
    state = game.state
    print("\n" + "=" * 52)
    print(f"DAY {state.day} — {state.time_of_day.value.upper()}")
    print("=" * 52)
    print(f"Logistics: {state.logistics}")
    if state.player:
        print(f"{state.player.describe()}")
    print()


def run_terminal(game: Game) -> None:
    print("SIX MONTHS")
    print("A grounded survival RPG")
    print()

    game.set_player(create_character())

    print("\nCharacter created.")
    print(f"You are {game.state.player.describe()}.")
    print(f"Background: {game.state.player.background}")

    while game.state.running:
        show_state(game)
        print("What do you do?")
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
