"""Evaluate a player's guess against a secret string."""


def evaluate_guess(secret: str, guess: str) -> str:
    """Evaluates a player's guess against a secret string.

   The function compares a given guess to a secret string of the same length,
   returning feedback to indicate correct and incorrect characters.
   The feedback uses the following symbols:
   1.`'+'`: Indicates that the character at the corresponding index matches the secret exactly.
   2. `'-'`: Indicates that the character is in the secret but not in the correct position.
   3. `' '`: Indicates that the character is not present in the secret.

   Args:
       secret (str): The secret string that the player's guess is compared against.
       guess (str): The player's guess string, which should be no longer than 4 characters.

   """
    feedback = []
    if len(guess) > 4:
        raise ValueError("Too long, I accept only guesses that are 4 characters or less.")

    for index, char in enumerate(guess):
        if char == secret[index]:
            feedback.append('+')
        elif char in secret:
            feedback.append('-')
        else:
            feedback.append(' ')

    return ''.join(feedback)
