from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class GameState:
    round: int = 1
    user_score: int = 0
    bot_score: int = 0
    user_bomb_used: bool = False
    bot_bomb_used: bool = False
    history: List[Dict] = field(default_factory=list)

    def is_game_over(self):
        return self.round > 3
