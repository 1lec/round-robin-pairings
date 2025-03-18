from tkinter import filedialog


class Player:
    """Represents a player in a tournament."""

    def __init__(self, name, position):
        self._name = name
        self._position = position

    def get_name(self):
        """Return the name of the player."""
        return self._name
    
    def get_position(self):
        """Return the position of the player within the Berger graph."""
        return self._position

class Tournament:
    """Represents a chess tournament with rounds and players."""

    def __init__(self):
        self._players = []

    def _read_player_names(self):
        """Prompts the user for a file, and reads the player names from the file."""
        with open(filedialog.askopenfilename(), 'r') as infile:
            for num, name in enumerate(infile):
                self._players.append(Player(name.rstrip(), num))

    def run(self):
        """Prompts user for players and tournament details, and writes out pairings to a file."""
        self._read_player_names()


def main():
    tournament = Tournament()
    tournament.run()


if __name__ == "__main__":
    main()
