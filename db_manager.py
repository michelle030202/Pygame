"""Handles Database interactions."""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Db:
    """A class to handle interactions with a Firebase Firestore database.

   The `Db` class initializes a connection to Firebase using credentials from a JSON file
   and provides methods to save and retrieve scores for players.

   Attributes:
       cred (firebase_admin.credentials.Certificate): Firebase credentials for authentication.
       db (firebase_admin.firestore.client): A Firestore client instance used
       for database interactions.
    """

    def __init__(self):
        """
        Initializes the `Db` class by setting up Firebase credentials and a Firestore client.

        """

        self.cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def save_score(self, player_name, attempts, time_taken):
        """
        Saves a player's score information to the Firestore database.

        Args:
            player_name (str): The name of the player whose score is being saved.
            attempts (int): The number of attempts the player took.
            time_taken (float): The time in seconds it took the player to guess the number.

        """
        player_ref = self.db.collection('players').document(player_name)
        player_ref.set({
            'attempts': attempts,
            'time_taken': time_taken
        })

    def get_best_score(self, player_name):
        """
        Retrieves the best score record for a specific player from the Firestore database.

        This method fetches the document associated with a player's name.
        If the record exists, it returns the corresponding data.

        Args:
            player_name (str): The name of the player whose score data is being retrieved.

        """
        player_ref = self.db.collection('players').document(player_name)
        player_data = player_ref.get()
        if player_data.exists:
            return player_data.to_dict()
        return None
