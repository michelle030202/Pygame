"""Test case for evaluate_guess module."""

import pytest
from main import evaluate_guess

# Define test cases
test_cases = [
    ('1234', '5678', '    '),  # No correct digits
    ('1234', '1678', '+   '),  # One correct digit in the correct position
    ('1234', '1243', '++--'),  # Two correct digits in correct positions
    ('1234', '4321', '----'),  # All digits correct but in wrong positions
]


# Parametrize the test function with test cases
@pytest.mark.parametrize("secret, guess, expected_feedback", test_cases)
def test_evaluate_guess(secret, guess, expected_feedback):
    """Tests the evaluate_guess function with various input cases.

    Args:
        secret (str): The secret string used as a reference for comparison.
        guess (str): The string provided as a guess to compare against the secret.
        expected_feedback (any): The expected output of the evaluate_guess function.

    Returns:
        None

    Raises:
        AssertionError: If the feedback returned by evaluate_guess does not
        match the expected output.
    """
    feedback = evaluate_guess(secret, guess)
    assert feedback == expected_feedback
