"""Calculate the score based on a specific formula."""


def calculate_score(guesses: int, time_taken: float) -> float:
    """Calculate the score based on the number of guesses and the time taken.

    Args:
        guesses (int): Number of guesses taken.
        time_taken (float): Time taken to guess in seconds.

    Returns:
        float: The calculated score.
    """
    return max(100 - guesses - time_taken / 60, 0)  # scoring formula
