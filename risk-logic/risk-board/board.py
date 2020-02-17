'''Modules'''
from typing import List, Tuple, Dict, Callable
import functools


class Player:
    '''Declaration of Player Class'''
    def __init__(self):
        self.contr_states: List[int] = [0] * 42
        self.cards: List[Tuple[int, int]] = []
        self.is_alive: bool = True

    def get_count(self) -> int:
        '''Gets the total number of troops a player has'''
        return sum(self.contr_states)

    def get_state_num(self) -> int:
        '''Gets the number of states a player owns'''
        return functools.reduce(
            lambda a, b: a + b,
            [1 if count_reinf > 0 else 0 for count_reinf in self.contr_states])


def reinf_num(player: Player) -> int:
    '''
        Determines number of reinforcements a player gets at beginning of turn
    '''
    countr_reinf: int = int(player.get_state_num() / 3)
    countr_reinf = countr_reinf if countr_reinf > 3 else 3

    contr_bonus: List[int] = [3, 7, 2, 5, 5, 2]
    is_contr_bonus: List[bool] = [True] * 6

    for i in range(len(player.contr_states)):
        if i < 6:
            is_contr_bonus[0] = (is_contr_bonus[0]
                                 and player.contr_states[i] == 0)
        elif i < 18:
            is_contr_bonus[1] = (is_contr_bonus[1]
                                 and player.contr_states[i] == 0)
        elif i < 22:
            is_contr_bonus[2] = (is_contr_bonus[2]
                                 and player.contr_states[i] == 0)
        elif i < 29:
            is_contr_bonus[3] = (is_contr_bonus[3]
                                 and player.contr_states[i] == 0)
        elif i < 38:
            is_contr_bonus[4] = (is_contr_bonus[4]
                                 and player.contr_states[i] == 0)
        else:
            is_contr_bonus[5] = (is_contr_bonus[5]
                                 and player.contr_states[i] == 0)
    for i, is_bonus in enumerate(is_contr_bonus):
        if is_bonus:
            countr_reinf += contr_bonus[i]

    return countr_reinf


class Board:
    '''Declaration of Board Class'''
    def __init__(self, num_players) -> None:
        self.countries: List[List[int]] = [
            # AFRICA [0-5]
            [1, 2, 3, 4, 5, 10],     # 0. East Africa
            [0, 5, 26],              # 1. Egypt
            [0, 4, 5],               # 2. Congo
            [0, 4],                  # 3. Madagascaar
            [0, 2, 3],               # 4. South Africa
            [0, 1, 2, 26, 28, 39],   # 5. North Africa

            # ASIA [6-17]
            [7, 10, 13, 16, 27],     # 6. Afghanistan
            [6, 10, 12, 13],         # 7. India
            [9, 11, 15, 17],         # 8. Irtkutsk
            [8, 11, 14, 17, 29],     # 9. Kamchatka
            [0, 6, 7, 26, 27],       # 10. Middle East
            [8, 9, 13, 14, 15],      # 11. Mongolia
            [7, 13, 21],             # 12. Siam
            [6, 7, 8, 11, 12, 16],   # 13. China
            [9, 11],                 # 14. Japan
            [8, 11, 13, 16, 17],     # 15. Siberia
            [6, 13, 15, 27],         # 16. Ural
            [8, 9, 11, 15],          # 17. Yakutsk

            # AUSTRALIA [18-21]
            [19, 20],                # 18. Eastern Australia
            [18, 20, 21],            # 19. New Guniea
            [18, 19, 21],            # 20. Western Australia
            [12, 19, 20],            # 21. Indonesia

            # EUROPE [22-28]
            [23, 24, 25, 28],        # 22. Great Britain
            [22, 25, 33],            # 23. Iceland
            [22, 25, 26, 27, 28],    # 24. Northern Europe
            [22, 23, 24, 27],        # 25. Scandinavia
            [1, 5, 10, 24, 27, 28],  # 26. Southern Europe
            [6, 10, 13, 24, 25, 26],  # 27. Ukraine
            [5, 22, 24, 26],         # 28. Western Europe

            # NORTH AMERICA [29-37]
            [9, 30, 34],             # 29. Alaska
            [29, 34, 35, 36],        # 30. Alberta
            [32, 36, 41],            # 31. Central America
            [31, 35, 36, 37],        # 32. Eastern United States
            [23, 34, 35, 37],        # 33. Greenland
            [29, 30, 33, 35],        # 34. Northwest Territory
            [30, 32, 33, 34, 36, 37],  # 35. Ontario
            [30, 31, 32, 35],        # 36. Western United States
            [32, 33, 35],            # 37. Quebec

            # SOUTH AMERICA [38-41]
            [39, 40],                # 38. Argentina
            [5, 38, 40, 41],         # 39. Brazil
            [38, 39, 41],            # 40. Peru
            [31, 39, 40]             # 41. Venezuela
        ]

        self.players: List[Player] = []
        for _ in range(num_players):
            self.players.append(Player())

        self.curr_stage: int = 0
        self.taken_count: List[int] = [0] * 42
        self.player_turn: int = 0
        self.stage_num: int = 0

    # Note: Currently assumes
    def set_board(self) -> None:
        '''Stage 1: Placing Troops'''
        print()
        print(self.taken_count)
        print(f'Player {self.player_turn} countr. num: ')

        new_count: int = -1
        while ((new_count < 0 or new_count > 41)
               or self.taken_count[new_count] != 0):
            new_count = int(input())

        self.players[self.player_turn].contr_states[new_count] = 1
        self.taken_count[new_count] = 1

        if 0 not in self.taken_count:
            self.curr_stage += 1
            self.player_turn = len(self.players) - 1

    def reinf_count(self) -> None:
        '''Stage 2: Fortifying Troops'''
        print()
        print(self.players[self.player_turn].contr_states)

        cont_stage: bool = functools.reduce(
            lambda a, b: a or b,
            [pl.get_count() <= 25 for pl in self.players])

        if not cont_stage:
            self.curr_stage += 1
            self.player_turn = len(self.players) - 1

        if self.players[self.player_turn].get_count() >= 25:
            return

        print(f'Player {self.player_turn} countr. num: ')

        new_count: int = -1
        while ((new_count < 0 or new_count > 41)
               or self.players[self.player_turn].contr_states[new_count] == 0):
            new_count = int(input())

        self.players[self.player_turn].contr_states[new_count] += 1

    def battle(self) -> None:
        '''Stage 3: Normal Battling'''
        print()
        print('BATTLE')
        print(f'Player {self.player_turn}: ')
        print(self.players[self.player_turn].contr_states)

        # Fortify Troops
        reinfr_tr: int = reinf_num(self.players[self.player_turn])

        # TODO: Give option to exchange cards for troops if possible

        while reinfr_tr > 0:
            print(f'Player {self.player_turn} Num Reinf: {reinfr_tr}')
            print('Enter Country Num: ')
            new_count: int = -1
            while (self.players[self.player_turn].contr_states[new_count] == 0
                   or (new_count < 0 or new_count > 41)):
                new_count = int(input())
            self.players[self.player_turn].contr_states[new_count] += 1
            reinfr_tr -= 1

        # Battle
        is_end_turn: bool = False
        while not is_end_turn:
            # TODO: Battle Step
            is_end_turn = True

        # TODO: Give option to move troops

    def turn(self) -> None:
        '''Method Executing Turn Based on Stage Num'''
        stages: Dict[int, Callable[[], None]] = {
            0: self.set_board,
            1: self.reinf_count,
            2: self.battle
        }

        stages[self.curr_stage]()
        self.player_turn = (self.player_turn + 1) % len(self.players)
