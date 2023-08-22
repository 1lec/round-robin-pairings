from classes import *

ASU_Open = Tournament('ASU Open', 'August 22nd, 2023', 'Tempe, Arizona')
round_dict = ASU_Open.pair_single_round_robin()

# print test
for round_num in round_dict:
    print(round_dict[round_num].get_pairings())
