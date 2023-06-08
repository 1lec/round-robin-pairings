class Player:
    """Represents a player in a chess tournament with 4 private data members: name, previous_opponents,
    previous_colors, and rounds_paired."""

    def __init__(self, name):
        self._name = name
        self._previous_opponents = set()  # Using a set to eliminate potential for duplicates.
        self._previous_colors = []  # Colors are sorted from least to most recently played.
        self._rounds_paired = 0

    def get_name(self):
        """Returns the name of a player."""

        return self._name

    def get_previous_opponents(self):
        """Returns the previous opponents of a player."""

        return self._previous_opponents

    def get_previous_colors(self):
        """Returns the previous colors the player has had."""

        return self._previous_colors

    def get_rounds_paired(self):
        """Return the number of rounds a player has paired."""

        return self._rounds_paired

    def add_opponent(self, player_object):
        """Takes a player object as an argument and adds it to a different player's list of previous opponents."""

        self._previous_opponents.add(player_object)

    def add_color(self, color):
        """Takes a string as an argument and appends it to the players list of previous colors."""

        self._previous_colors.append(color)


class Round:
    """Represents a round in a chess tournament with two private data members: round_number and pairings."""

    def __init__(self, round_number):

        self._round_number = round_number
        self._pairings = set()  # Using a set to eliminate potential for duplicates.

    def get_round_number(self):
        """Returns the round number of a round object."""

        return self._round_number

    def get_pairings(self):
        """Returns the pairings for a round."""

        return self._pairings

    def add_pairing(self, pairing):
        """Takes a pairing as an argument and adds it to the set of pairings for the round."""

        self._pairings.add(pairing)
