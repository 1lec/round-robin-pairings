from classes import Player
from classes import Round

# Step 1: Read names of players from a file. Pass these names to Step 2 in the form of a list. An example list is:
# [Carlsen, Caruana, Nakamura, So]

players_list = ['Carlsen', 'Caruana', 'Nakamura', 'So', 'Sevian', 'Shakland', 'Anand', 'Shirov']

# Step 2: From the list of players, create a dictionary of objects, with the player's name as the key and a Player
# object as the value. This step is necessary because I am not sure how to generate a list of Player objects from a
# list of strings. An example dictionary is:
# {'Carlsen': Player('Carlsen'), 'Caruana': Player('Caruana'), 'Nakamura': Player('Nakamura'), 'So': Player('So')}

player_object_dict = {}

for names in players_list:
    player_object_dict[names] = Player(names)

# Step 3: Loop through the dictionary of Player objects to create a list of Player objects. This will be necessary to
# reorder the Player objects at a later step. An example list is:
# [Player('Carlsen'), Player('Caruana'), Player('Nakamura'), Player('So')]

player_object_list = []

for names in player_object_dict:
    player_object_list.append(player_object_dict[names])

# Step 4: From the length of the list of Player objects, create a dictionary of rounds, with the round number as the
# key and a Round object as the value. An example dictionary is:
# {1: Round(1), 2: Round(2), 3: Round(3)}

round_dictionary = {}

count = 1

while count < len(player_object_list):
    round_dictionary[count] = Round(count)
    count += 1

# Step 5: Loop through the dictionary of rounds, and for each round, loop through the list of Player objects. For each
# Player, if the number of rounds they've been paired is less than the current round that is being paired, find an
# unpaired opponent for the player by again looping through the list of Player objects.

# Step 6: Once an unpaired opponent is found for the player, determine the colors by comparing the number of whites
# played by both players. If they have played the same number of whites, compare their most recent colors played, loop
# through their list of colors played until a difference is found. Once a difference is found, give white to player
# who played black. If the players have played the exact same number of whites in the same order, give a random player
# white.

# Step 7: Once a pairing is determined, create a tuple in the form of (white_player, black_player) and add it to the
# set of pairings contained within the current Round object. Add 1 to the rounds_played for both players, and update
# each player's colors_played and white_count accordingly.

# Step 8a: If no unpaired opponent was found for a player, the round must be repaired, which requires a few steps to
# reset. First, for those players who were already paired (and thus need to be repaired), remove the last player in
# their list of previous opponents, remove their most recently played color (and if that color was white, subtract 1
# from their white_count), and reset their number of rounds paired to the previous round. Finally, empty the set of
# pairings for the current Round object.

# Step 8b: Once the invalid pairings from Step 2 are reset, shuffle the list of Player objects and reiterate through
# the Round. Continue this step until a valid set of pairings is obtained, returning to Step 8a as needed. A set of
# pairings is valid once the length of set is equal to half the number of Player objects.

# Step 9: Once a valid set of pairings is obtained for every Round object, write the round number and corresponding
# pairings into a new file.
