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

# Step 5: Once an unpaired opponent is found for the player, determine the colors.
