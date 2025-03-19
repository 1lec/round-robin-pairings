from tkinter import filedialog


class Position:
    """Represents a position in a round robin schedule span diagram."""

    def __init__(self, number, color, opponent, player):
        self._number = number
        self._color = color
        self._opponent = opponent
        self._player = player

    def get_color(self):
        """Return the color of this position."""
        return self._color
    
    def get_opponent(self):
        """Return the opponent number for the given position."""
        return self._opponent
    
    def get_player(self):
        """Return the player of this position."""
        return self._player
    
    def set_player(self, player):
        """Receives a player object and assigns it to self._player."""
        self._player = player

    def swap_color(self):
        """Changes the color of the position from white to black, or vice versa."""
        self._color = 'white' if self._color == 'black' else 'black'


class Pairing:
    """Represents a pairing in a chess tournament."""

    def __init__(self, white, black):
        self._white = white
        self._black = black

    def get_white_player(self):
        """Return the white player for this pairing."""
        return self._white
    
    def get_black_player(self):
        """Return the black player for this pairing."""
        return self._black


class BergerTable:
    """Represents a Berger table, a tabular representation of a round robin tournament schedule."""

    def __init__(self, players):
        self._players = players
        self._rounds = {}
        self._fixed_position = len(self._players) - 1
        self._positions = {}
        self._opponents = {}
        self._rotation_factor = len(self._players) // 2 * -1

    def _initialize_rounds(self):
        """Initialize the list of rounds for the table."""
        for num in range(1, len(self._players)):
            self._rounds[num] = Round(num)

    def _determine_opponents(self):
        """Create a dictionary that tracks which positions are slated to play each round."""
        low = self._fixed_position // 2
        high = low + 1
        while low > -1:
            self._opponents[low] = high
            self._opponents[high] = low
            low -= 1
            high += 1

    def _initialize_positions(self):
        """Initialize the dictionary of positions and assign each player to their starting position."""
        for num in range(len(self._players)):
            color = 'white' if num < self._fixed_position / 2 else 'black'
            opponent = self._opponents[num]
            player = self._players[num]
            self._positions[num] = Position(num, color, opponent, player)

    def _pair_round(self, round_number):
        """Use the current alignment of players within the positions to pair the given round."""
        for num in range(len(self._positions)):
            current_position = self._positions[num]
            if current_position.get_color() == 'white':
                white = current_position.get_player()
                black = self._positions[current_position.get_opponent()].get_player()
                self._rounds[round_number].add_pairing(white, black)
        if round_number % 2 == 0:
            self._rounds[round_number].move_last_to_first()

    def _rotate_players(self):
        """Except for the player in the fixed position, rotate the position of the players to obtain new pairings."""
        for player in self._players:
            if player.get_position() != self._fixed_position:
                player.change_position(self._rotation_factor)
            if player.get_position() < 0:
                player.change_position(self._fixed_position)
            new_position = player.get_position()
            self._positions[new_position].set_player(player)

    def _swap_first_board_colors(self):
        """Swaps colors for first and last positions to ensure player in fixed position alternates colors."""
        self._positions[0].swap_color()
        self._positions[self._fixed_position].swap_color()

    def get_rounds(self):
        """Returns all rounds for the Berger Table."""
        return self._rounds

    def create_table(self):
        """Given a list of players, this method creates a Berger table."""
        self._initialize_rounds()
        self._determine_opponents()
        self._initialize_positions()
        for num in range(len(self._rounds)):
            self._pair_round(num + 1)
            self._rotate_players()
            self._swap_first_board_colors()


class Round:
    """Represents a round of a chess tournament."""

    def __init__(self, number):
        self._number = number
        self._pairings = []

    def get_round_number(self):
        """Returns the round number."""
        return self._number

    def add_pairing(self, white_player, black_player):
        """Adds a pairing to the list of the pairings."""
        self._pairings.append(Pairing(white_player, black_player))

    def get_pairings(self):
        """Returns the pairings for the round."""
        return self._pairings
    
    def move_last_to_first(self):
        """Moves the last pairing in the list to the front."""
        last = self._pairings[-1]
        self._pairings.pop(-1)
        self._pairings.insert(0, last)


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
    
    def change_position(self, delta_position):
        """Changes the position of the player by delta position."""
        self._position += delta_position


class Tournament:
    """Represents a chess tournament with rounds and players."""

    def __init__(self):
        self._players = []
        self._schedule = None

    def _read_player_names(self):
        """Prompts the user for a file, and reads the player names from the file."""
        with open(filedialog.askopenfilename(), 'r') as infile:
            for num, name in enumerate(infile):
                self._players.append(Player(name.rstrip(), num))

    def _generate_schedule(self):
        """Takes the list of players from the file and generates a round robin schedule."""
        schedule = BergerTable(self._players)
        schedule.create_table()
        self._schedule = schedule

    def _write_schedule(self):
        """Prompts the user for a file, then writes the schedule to said file."""
        with open(filedialog.askopenfilename(), 'w') as outfile:
            pass

    def _print_schedule(self):
        """Test method that prints the schedule to the terminal."""
        rounds = self._schedule.get_rounds()
        for num in range(1, len(self._players)):
            print(f"Round {num}")
            pairings = rounds[num].get_pairings()
            for pairing in pairings:
                print(f"{pairing.get_white_player().get_name()} - {pairing.get_black_player().get_name()}")

    def run(self):
        """Prompts user for players and tournament details, and writes out pairings to a file."""
        self._read_player_names()
        self._generate_schedule()
        self._print_schedule()


def main():
    tournament = Tournament()
    tournament.run()


if __name__ == "__main__":
    main()
