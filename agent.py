# Entry point for Rock–Paper–Scissors–Plus referee agent
# Run using: python agent.py

from state import GameState
from tools import validate_move, resolve_round, update_game_state


def explain_rules():
    print(
        "\nWelcome to Rock–Paper–Scissors–Plus!\n"
        "Rules:\n"
        "• Best of 3 rounds\n"
        "• Moves: rock, paper, scissors, bomb\n"
        "• Bomb can be used only once\n"
        "• Invalid input wastes the round\n"
    )


def get_user_move():
    return input("Enter your move: ")


def play_game():
    state = GameState()
    explain_rules()

    while not state.is_game_over():
        print(f"\n--- Round {state.round} ---")

        user_input = get_user_move()
        is_valid, result = validate_move(user_input, state)

        # Handle invalid input
        if not is_valid:
            print(f"❌ {result}")
            print("Allowed moves: rock, paper, scissors, bomb")
            state.round += 1
            continue

        # Resolve round and update state
        round_result = resolve_round(result, state)
        state = update_game_state(round_result, state)

        winner = round_result["winner"].capitalize()

        print(
            f"👤 You played: {round_result['user_move']}\n"
            f"🤖 Bot played: {round_result['bot_move']}\n"
            f"🏆 Round winner: {winner}"
        )

        # Explicit bomb usage feedback
        if round_result["user_move"] == "bomb":
            print("💣 You have used your bomb. It cannot be used again.")

        if round_result["bot_move"] == "bomb":
            print("🤖 Bot has used its bomb.")

    # Game over summary
    print("\n=== GAME OVER ===")
    print(f"📊 Final Score → You: {state.user_score} | Bot: {state.bot_score}")

    if state.user_score > state.bot_score:
        print("🏆 You win the game!")
    elif state.bot_score > state.user_score:
        print("🤖 Bot wins the game!")
    else:
        print("🤝 The game is a draw!")


if __name__ == "__main__":
    play_game()
