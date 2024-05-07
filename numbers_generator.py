"""Generate a random four-digit number."""

import random


def generate_number() -> str:
    """Generate a random four-digit number with no duplicate digits.

    Returns:
        str: A string representing the four-digit number.
    """
    numbers = random.sample(range(10), 4)
    return ''.join(map(str, numbers))
