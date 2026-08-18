from six_months.engine.game import Game


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

    if not game.state.player_name:
        name = input("What is your name? ").strip()
        game.state.player_name = name or "Unknown"

    while game.state.running:
        show_state(game)
        print(f"You are {game.state.player_name}.")
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
