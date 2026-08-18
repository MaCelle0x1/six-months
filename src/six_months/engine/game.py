from .state import GameState


class Game:
    """Owns the top-level game state and time progression."""

    def __init__(self, state: GameState | None = None) -> None:
        self.state = state or GameState()

    def start(self) -> None:
        self.state.running = True

    def set_player(self, character) -> None:
        self.state.player = character

    def advance(self) -> None:
        self.state.advance_time()
