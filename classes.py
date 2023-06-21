class Player:
    """Represents a player in a chess tournament with 5 private data members: name, previous_opponents,
    previous_colors, white_count and rounds_paired."""

    def __init__(self, name):
        self._name = name
        self._previous_opponents = set()  # Using a set to eliminate potential for duplicates.
        self._previous_colors = []  # Most recent color is at the front of the list.
        self._white_count = 0
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

    def get_white_count(self):
        """Returns the number of whites the player has had."""

        return self._white_count

    def get_rounds_paired(self):
        """Return the number of rounds a player has paired."""

        return self._rounds_paired

    def add_opponent(self, player_object):
        """Takes a player object as an argument and adds it to a different player's list of previous opponents."""

        self._previous_opponents.add(player_object)

    def add_black(self):
        """Adds a black to the front of the previous_colors data member."""

        self._previous_colors.insert(0, 'B')

    def add_white(self):
        """Increases the number of whites a player has had by 1, and adds a white to the front of the previous_colors
        data member."""

        self._previous_colors.insert(0, 'W')
        self._white_count += 1

    def subtract_white(self):
        """Decreases the number of whites a player has had by 1. This method is necessary for removing invalid
        pairings."""

        self._white_count -= 1

    def determine_colors(self, player_object):
        """Takes a player object as an argument and determine due colors between that object and the object the method
        is being called upon."""

        if self._white_count > player_object.get_white_count():
            self.add_black()
            player_object.add_white()

        elif self._white_count < player_object.get_white_count():
            self.add_white()
            player_object.add_black()

        else:
            same_color = True

            for i, color in enumerate(self._previous_colors):
                if color != player_object.get_previous_colors()[i]:
                    same_color = False

            if

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
