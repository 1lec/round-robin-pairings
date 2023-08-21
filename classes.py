import random

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

    def add_opponent(self, player_object):
        """Takes a player object as an argument and adds it to a different player's list of previous opponents. Also
        increases the number of rounds paired for both player and opponent by 1."""

        self._previous_opponents.append(player_object)
        self._rounds_paired += 1

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
            color_list_1 = self._previous_colors
            color_list_2 = player_object.get_previous_colors()

            if color_list_1 == color_list_2:
                self.add_white()
                player_object.add_black()

            else:
                for i, color in enumerate(self._previous_colors):

                    if color != player_object.get_previous_colors()[i]:  # if a color mismatch is found

                        if self._previous_colors[i] == 'W':
                            self.add_black()
                            player_object.add_white()
                            break

                        else:
                            self.add_white()
                            player_object.add_black()
                            break

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


class Tournament:
    """Represents a chess tournament with rounds and players."""

    def __init__(self, title, date, location):
        self._title = title
        self._date = date
        self._location = location
        self._round_dict = {}

    def pair_single_round_robin(self, players_list):
        """Takes as an argument a list of players and generates single round-robin pairings for the event."""

        # Step 1: Read names of players from a file. Pass these names to Step 2 in the form of a list. An example list is:
        # [Carlsen, Caruana, Nakamura, So]

        players_list = ['Carlsen', 'Caruana', 'Nakamura', 'So', 'Sevian', 'Shankland', 'Anand', 'Shirov']

        # Step 2: Use list comprehension to generate a list of player objects from the list of player names.

        player_object_list = [Player(player) for player in players_list]

        # Step 4: From the length of the list of Player objects, create a dictionary of rounds, with the round number as the
        # key and a Round object as the value. An example dictionary is:
        # {1: Round(1), 2: Round(2), 3: Round(3)}

        round_dict = {}

        count = 1

        while count < len(player_object_list):
            round_dict[count] = Round(count)
            count += 1

        # Step 5: Loop through the dictionary of rounds, and for each round, loop through the list of Player objects. For each
        # Player, if the number of rounds they've been paired is less than the current round that is being paired, find an
        # unpaired opponent for the player by again looping through the list of Player objects.

        for round_num in round_dict:  # loop through each round in the dictionary of rounds
            while round_dict[round_num].is_incomplete(player_object_list):
                for player_1 in player_object_list:  # for each round, find an unpaired player in the list of Player objects
                    paired = player_1.get_rounds_paired() == round_num
                    while player_1.get_rounds_paired() < round_num:
                        for player_2 in player_object_list:
                            if player_1.is_valid_opponent(player_2, round_num):
                                player_1.determine_colors(player_2)
                                round_dict[round_num].generate_pairing(player_1, player_2)
                                paired = True
                                break
                    if not paired:
                        round_dict[round_num].reset_round(player_object_list)
                        random.shuffle(player_object_list)
