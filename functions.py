from classes import Round

def generate_rounds(players_list):
    """Takes a list of players as an argument and returns a dictionary with round numbers as keys and round objects
    as values. The number of key-value pairs is equivalent to one less than the number of players."""

    number_of_rounds = len(players_list) - 1

    round_dict = {}

    count = 0
    while count < number_of_rounds:
        round_dict[count + 1] = Round(count + 1)
        count += 1

    return round_dict
