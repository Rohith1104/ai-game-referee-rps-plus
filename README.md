AI Game Referee — Rock–Paper–Scissors–Plus

Overview

This project implements a stateful AI referee agent for a modified Rock-Paper-Scissors game (“Rock-Paper-Scissors-Plus”).
The agent runs a best-of-3 game between a user and the bot, enforces game rules, tracks state across turns, and provides clear, round-by-round feedback.

The goal of this assignment was not UX polish, but correctness of logic, clarity of state modeling, and clean separation of agent responsibilities.

Game Rules (Agent-Enforced)

Best of 3 rounds

Valid moves: rock, paper, scissors, bomb

bomb beats all other moves

bomb vs bomb → draw

Each player can use bomb only once per game

Invalid input wastes the round

Game automatically ends after 3 rounds

State Model

The game state is modeled explicitly using a GameState dataclass (state.py).

Tracked state includes:

Current round number

User and bot scores

Bomb usage flags for both players

Round history (moves and outcomes)

State is persisted across turns and never stored implicitly in prompts, ensuring predictable and debuggable behavior.

Tool Design

Game logic is implemented via explicit tools (tools.py), not inside the agent loop.

Tools:

validate_move

Validates user input

Enforces allowed moves

Enforces single-use bomb constraint

Returns structured success/failure responses

resolve_round

Selects the bot’s move (with bomb constraint)

Applies game rules to determine the round winner

Returns a structured round result

update_game_state

Mutates the game state safely

Updates scores, round count, bomb usage, and history

This separation ensures that intent validation, game logic, and state mutation are clearly isolated.

Agent Flow

The agent (agent.py) is responsible only for:

Explaining rules (≤ 5 lines)

Prompting the user

Calling tools in the correct order

Rendering user-facing responses

Automatically terminating the game

The conversational loop cleanly follows:
Input → Validation → Resolution → State Update → Response

Tradeoffs

Implemented as a CLI-style conversational loop instead of a UI or server, as per assignment constraints

Bot move selection is random rather than strategy-based, prioritizing clarity over competitiveness

Possible Improvements

With more time, I would:

Add structured output schemas for better tool interoperability

Introduce deterministic bot strategies

Improve conversational intent handling (e.g., natural language inputs)

Add a lightweight chat UI (web or terminal-based) to visualize game state and history, while keeping agent logic unchanged.

How to Run
python agent.py

Final Notes

This implementation focuses on correctness, explainability, and clean agent architecture, aligning with real-world conversational agent design rather than prompt-only solutions.