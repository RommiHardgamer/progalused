class GameStats():
    """Check game statistics"""

    def __init__(self):
        """Initialize statistics."""

        self.game_active = False
        self.reset_stats()
        self.high_score = 0
    def reset_stats(self):
        """Initialize score and level, which can change during the game."""
        self.score = 0
        self.level = 1
        self.bonus = 0