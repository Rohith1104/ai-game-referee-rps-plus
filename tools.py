import random

# Allowed moves in the game
VALID_MOVES = ["rock", "paper", "scissors", "bomb"]


def validate_move(move: str, state):
    """
    Validates the user's move.
    Returns:
      (True, cleaned_move) if valid
      (False, reason) if invalid
    """
    if not move:
        return False, "No move provided. Round wasted."

    move = move.lower().strip()

    if move not in VALID_MOVES:
        return False, "Invalid move. Round wasted."

    if move == "bomb" and state.user_bomb_used:
        return False, "Bomb already used. Round wasted."

    return True, move


def resolve_round(user_move: str, state):
    """
    Determines bot move and resolves the round outcome.
    """
    bot_move = random.choice(VALID_MOVES)

    # Ensure bot uses bomb only once
    if bot_move == "bomb" and state.bot_bomb_used:
        bot_move = random.choice(["rock", "paper", "scissors"])

    # Determine winner
    if user_move == "bomb" and bot_move != "bomb":
        winner = "user"
    elif bot_move == "bomb" and user_move != "bomb":
        winner = "bot"
    elif user_move == bot_move:
        winner = "draw"
    elif (
        (user_move == "rock" and bot_move == "scissors") or
        (user_move == "paper" and bot_move == "rock") or
        (user_move == "scissors" and bot_move == "paper")
    ):
        winner = "user"
    else:
        winner = "bot"

    return {
        "user_move": user_move,
        "bot_move": bot_move,
        "winner": winner
    }


def update_game_state(round_result: dict, state):
    """
    Updates the game state after a round.
    """
    if round_result["user_move"] == "bomb":
        state.user_bomb_used = True

    if round_result["bot_move"] == "bomb":
        state.bot_bomb_used = True

    if round_result["winner"] == "user":
        state.user_score += 1
    elif round_result["winner"] == "bot":
        state.bot_score += 1

    state.history.append(round_result)
    state.round += 1

    return state
