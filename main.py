from classes import *

ASU_Open = Tournament('ASU Open', 'August 22nd, 2023', 'Tempe, Arizona')
ASU_Open.pair_single_round_robin()
round_dict = ASU_Open.get_round_dict()

# print test
for round_num in round_dict:
    print(round_dict[round_num].get_pairings())
