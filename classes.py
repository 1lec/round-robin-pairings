class Player:
    """Represents a player in a chess tournament with 5 private data members: name, previous_opponents,
    previous_colors, white_count and rounds_paired."""

    def __init__(self, name):
        self._name = name
        self._previous_opponents = []  # Most recent opponent is at the end of the list.
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

    def increase_rounds_paired(self):
        """Increases the rounds_paired for a Player object by 1."""

        self._rounds_paired += 1

    def add_opponent(self, player_object):
        """Takes a player object as an argument and adds it to a different player's list of previous opponents. Also
        increases the number of rounds paired for both player and opponent by 1."""

        self._previous_opponents.append(player_object)
        self._rounds_paired += 1
        player_object.increase_rounds_paired()

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
            count = 0

            while same_color and (count < len(self._previous_colors)):
                for i, color in enumerate(self._previous_colors):

                    if color != player_object.get_previous_colors()[i]:  # if a color mismatch is found

                        if self._previous_colors[i] == 'W':
                            self.add_black()
                            player_object.add_white()

                        else:
                            self.add_white()
                            player_object.add_black()

                        same_color = False

            if same_color:
                self.add_white()
                player_object.add_black()

    def is_valid_opponent(self, player_2, current_round):
        """Takes as arguments a Player object and the current round number and returns True if that Player object can be
        paired with the Player object the method is called on."""

        unpaired = player_2.get_rounds_paired() < current_round

        return (self != player_2) and unpaired and (player_2 not in self.get_previous_opponents())

    def reset_player(self):
        """Method to be utilizes during a round-reset. Decreases rounds_paired by 1, removes the last opponent, and
        removes the last color played."""

        self._rounds_paired -= 1
        self._previous_opponents.pop(-1)
        self._previous_colors.pop(0)


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

    def generate_pairing(self, player_1, player_2):
        """Takes two Player objects as arguments and adds their pairing to the set of pairings for the round. Also
        updates each player's list of previous opponents."""

        if player_1.get_previous_colors()[0] == 'W':
            new_pairing = (player_1.get_name(), player_2.get_name())
            self.add_pairing(new_pairing)
            player_1.add_opponent(player_2)
            player_2.add_opponent(player_1)

        else:
            new_pairing = (player_2.get_name(), player_1.get_name())
            self.add_pairing(new_pairing)
            player_1.add_opponent(player_2)
            player_2.add_opponent(player_1)

    def is_incomplete(self, player_list):
        """Takes the list of players competing in the tournament as an argument and returns True if the set of pairings
        for a Round object is incomplete. A set of pairings for a round is incomplete if the length of the set is less
        than half the number of players competing in the tournament."""

        return len(self.get_pairings()) < (len(player_list) // 2)

    def reset_round(self, player_list):
        """Takes a list of player objects as an argument. Deletes any pairings created for a round and makes necessary
        changes to all Player objects in the list by calling the reset_player method from the Player class."""

        self._pairings.clear()

        for player in player_list:
            if player.get_rounds_paired() == self._round_number:
                player.reset_player()
