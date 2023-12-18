# Round Robin Pairings

Round Robin Parings generates pairings for a single round-robin chess tournament with an even number of players.

## Usage:

From a text file containing [player names](example_players.txt), generate a text file containing [complete
single-round-robin pairings](example_pairings.txt).

## Instructions:

1. Download [roundrobin.py](roundrobin.py).
2. This program was written in Python 3, which you will need to run the program. You can download the latest version
[here](https://www.python.org/downloads/).
3. To run the program, open your command prompt and navigate to the folder where you stored roundrobin.py. Once in the
correct folder, type `python3 roundrobin.py`.
4. After answering some questions about your tournament, you will be prompted for a text file containing the names of
the players in your event. Be sure to follow the same format as the [provided example](example_players.txt).
5. The program will now pair the tournament. Once it is complete, you will be prompted to save the pairings to your
computer.
6. Locate and open your saved file to view the pairings for your tournament!

## Limitations:

* Only events with an even number of players can be paired.
* With regard to speed, this program is not recommended for events with over 16 players. Fortunately, few round-robin
events should exceed this number of players.