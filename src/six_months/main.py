from six_months.engine.game import Game
from six_months.ui.terminal import run_terminal


def main() -> None:
    game = Game()
    game.start()
    run_terminal(game)


if __name__ == "__main__":
    main()
