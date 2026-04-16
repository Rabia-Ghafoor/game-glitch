def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200  # FIX: was 1–50, which was easier than Normal
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).
    FIX: always compare as ints — no more string coercion on even attempts.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"  # FIX: message was swapped (said Go HIGHER)
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.
    FIX 1: win points use attempt_number directly, no +1 offset.
    FIX 2: "Too High" always penalises — no +5 bonus on even attempts.
    """
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)  # FIX: was attempt_number + 1
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5  # FIX: was +5 on even attempts for Too High

    return current_score