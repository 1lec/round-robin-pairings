import random
from tkinter import filedialog


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
        """Method to be utilized during a round-reset. Decreases rounds_paired by 1, removes the last opponent, and
        removes the last color played."""

        self._rounds_paired -= 1
        self._previous_opponents.pop(-1)
        self._previous_colors.pop(0)

    def total_player_reset(self):
        """Resets all data members for a Player."""

        self._rounds_paired = 0
        self._white_count = 0
        self._previous_colors.clear()
        self._previous_opponents.clear()


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
                if player.get_previous_colors()[0] == 'W':
                    player.subtract_white()
                player.reset_player()


class Tournament:
    """Represents a chess tournament with rounds and players."""

    def __init__(self, title, date, location):
        self._title = title
        self._date = date
        self._location = location
        self._round_dict = {}
        self._rounds_paired = 0

    def get_round_dict(self):
        """Returns the dictionary of Round objects for a Tournament."""

        return self._round_dict

    def total_reset(self, player_object_list):
        """Clears all pairings from each Round, and resets all data members for each Player."""

        self._rounds_paired = 0

        for player in player_object_list:
            player.total_player_reset()

        for num_round in self._round_dict:
            self._round_dict[num_round].get_pairings().clear()

    def pair_single_round_robin(self):
        """Takes as an argument a list of players and generates single round-robin pairings for the event."""

        # Step 1: Clear the current dictionary of pairings.

        self._round_dict.clear()

        # Step 2: Read from a file a list of names of players. An example list is:
        # ['Carlsen', 'Caruana', 'Nakamura', 'So']

        with open(filedialog.askopenfilename(), 'r') as infile:
            pre_players_list = infile.readlines()

        players_list = []

        for player_name in pre_players_list:
            players_list.append(player_name.rstrip())

        # Step 3: Use list comprehension to generate a list of player objects from the list of player names.

        player_object_list = [Player(player) for player in players_list]

        # Step 4: From the length of the list of Player objects, create a dictionary of rounds, with the round number as
        # the key and a Round object as the value. An example dictionary is:
        # {1: Round(1), 2: Round(2), 3: Round(3)}

        count = 1

        while count < len(player_object_list):
            self._round_dict[count] = Round(count)
            count += 1

        # Step 5: Generate a complete set of pairings for each Round object, starting with Round 1. If at some point
        # during the process of pairing a round, an opponent cannot be found for a player, the list of players is
        # shuffled and another attempt at pairing the round is made. If shuffling the list does not fix the issue, it's
        # possible (and maybe likely) that no legal set of pairings for the Round exists. In this case, all sets of
        # pairings of clear, and the process begins again from Round 1.

        while self._rounds_paired < len(player_object_list) - 1:
            for round_num in self._round_dict:
                shuffles = 0  # Represents the number of times player_object_list has been shuffled

                # While player_object_list has not been shuffled more than once and the current Round does not have a
                # complete set of pairings, attempt to generate a complete set of pairings.
                while shuffles < 2 and self._round_dict[round_num].is_incomplete(player_object_list):
                    for player_1 in player_object_list:
                        if player_1.get_rounds_paired() < round_num:
                            for player_2 in player_object_list:
                                if player_1.is_valid_opponent(player_2, round_num):
                                    player_1.determine_colors(player_2)
                                    self._round_dict[round_num].generate_pairing(player_1, player_2)
                                    break

                            # If an opponent was not found for player_1, delete the pairings for the current round,
                            # shuffle the list of Player objects, and try again to find a set of valid pairings.
                            if player_1.get_rounds_paired() < round_num:
                                self._round_dict[round_num].reset_round(player_object_list)
                                random.shuffle(player_object_list)
                                shuffles += 1
                                break

                # If the Round object has a complete set of pairings, attempt to pair the next round.
                if not self._round_dict[round_num].is_incomplete(player_object_list):
                    self._rounds_paired += 1

                # If a complete set of pairings could not be generated after one shuffle, delete all pairings and
                # restart from round 1.
                else:
                    self.total_reset(player_object_list)
                    break

        # Step 6: Write all pairings to a file.

        self.write_pairings_to_file()

    def write_pairings_to_file(self):
        """Writes the pairings currently stored in self._round_dict to a file."""

        with open(filedialog.asksaveasfilename(), 'w') as outfile:
            for round_num in self._round_dict:
                outfile.write('Round ' + str(round_num) + '\n')
                for pairing in self._round_dict[round_num].get_pairings():
                    outfile.write(pairing[0] + ' - ' + pairing[1] + '\n')
                outfile.write('\n')
