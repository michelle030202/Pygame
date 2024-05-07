"""A number-guessing game that generates a 4 digits number and prints feedback on each guess,
congratulations upon success, and performance metrics.  """

from time import time
from guess_evaluator import evaluate_guess
from numbers_generator import generate_number
from db_manager import Db


def main():
    """
    Runs the main game loop for a number-guessing game, prompting the user for their name
    and guesses.

   """
    player_name = input("Please enter your name: ")
    secret_number = generate_number()
    attempts = 0
    start_time = time()
    db_instance = Db()

    while True:
        guess = input("Enter your guess (four unique digits): ")
        attempts += 1
        feedback = evaluate_guess(secret_number, guess)
        print(f"Feedback: {feedback}")
        if feedback == '++++':
            end_time = time()
            time_taken = end_time - start_time
            print(f"Congratulations {player_name}! You guessed the number in {attempts} "
                  f"attempts and {time_taken:.2f}"
                  f" seconds.")
            db_instance.save_score(player_name, attempts, time_taken)
            best_score = db_instance.get_best_score(player_name)
            if best_score:
                print(f"Your best score: {best_score}")
            break


if __name__ == "__main__":
    main()
