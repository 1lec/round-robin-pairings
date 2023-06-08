# Step 1: Read names of players from a file. Pass these names to Step 2 in the form of a list.

# Step 2: From the list of players, create a dictionary of objects, with the player's name as the key and a Player
# object as the value. An example dictionary is:
# {'Carlsen': Player('Carlsen'), 'Caruana': Player('Caruana'), 'Nakamura': Player('Nakamura'), 'So': Player('So')}

# Step 3: From list of players, create a dictionary of rounds, with the round number as the key and a Round object
# as the value. An example dictionary is:
# {1: Round(1), 2: Round(2), 3: Round(3)}

# Step 4: Loop through the dictionary of rounds, and for each round, loop through the dictionary of players. For each
# player if the number of rounds they've been paired is less than the current round that is being paired, find an
# unpaired opponent for the player by again looping through the dictionary of players.

# Step 5: Once an unpaired opponent is found for the player, determine the colors by comparing the number of whites
# played by both players. If they have played the same number of whites, compare their most recent colors played, loop
# through their list of colors played until a difference is found. Once a difference is found, give white to player
# who played black. If the players have played the exact same number of whites in the same order, give a random player
# white.

# Step 6: Once a pairing is determined, create a tuple in the form of (white_player, black_player) and add it to the
# set of pairings contained within the current Round object. Add 1 to the rounds_played for both players, and update
# each player's colors_played and white_count accordingly.

# Step 7: If no unpaired opponent was found for a player, empty the set of pairings for the current Round object,
# shuffle the dictionary of players
