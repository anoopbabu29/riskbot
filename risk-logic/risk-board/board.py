'''Modules'''
from typing import List, Tuple, Dict, Any, Callable
import random
import functools


countries: List[List[int]] = [
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
NUM_COUNTRIES = len(countries)


def safe_input(args: Dict[str, Any], ind: str, inp_type):
    '''Gets input safely from type any dictionary'''
    if ind in args and isinstance(args[ind], inp_type):
        return args[ind]

    return None


def within_range(val: int, max_val: int = NUM_COUNTRIES) -> bool:
    '''Check whether in range of countries'''
    return 0 <= val < max_val


class Player:
    '''Declaration of Player Class'''
    def __init__(self) -> None:
        self.contr_states: List[int] = [0] * NUM_COUNTRIES
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


def battle_fort_phase(att_player: Player, num_reinf: int) -> None:
    '''Stage 3: Battle, Phase 1: Fortify Troops'''
    # TODO: Give option to exchange cards for troops if possible
    while num_reinf > 0:
        print(f'Num Reinf: {num_reinf}')
        print('Enter Country Num: ')
        new_count: int = -1
        while (not within_range(new_count)
               or att_player.contr_states[new_count] == 0):
            new_count = int(input())
        att_player.contr_states[new_count] += 1
        num_reinf -= 1


def battle_sel_count_step(att_player: List[int],
                          att_ind: int,
                          def_ind: int) -> Tuple[bool, int, int]:
    '''Stage 3: Battle, Phase 2: Battle, Step 1: Country Selection'''
    if not within_range(att_ind) or att_player[att_ind] < 2:
        print('Invalid Option (att)')
        return False, 0, 0

    if (not within_range(def_ind) or att_player[def_ind] != 0
            or def_ind not in countries[att_ind]):
        print('Invalid Option (def)')
        return False, 0, 0

    return True, att_ind, def_ind


def battle_rolls(roll_count: int) -> List[int]:
    '''Return Rolls in Risk Battle'''
    rolls: List[int] = []

    for _ in range(roll_count):
        rolls.append(random.randint(1, 6))
    rolls.sort(reverse=True)

    return rolls


def battle_roll_loss(att_rolls: List[int],
                     def_rolls: List[int]) -> Tuple[int, int]:
    '''Function determining troops lost'''
    num_att_loss: int = 0
    num_def_loss: int = 0

    while att_rolls != [] and def_rolls != []:
        if att_rolls[0] > def_rolls[0]:
            num_att_loss += 1
        else:
            num_def_loss += 1

    return num_att_loss, num_def_loss


def battle_battle_step(att_player: Player,
                       def_player: Player,
                       state_att: int,
                       state_def: int) -> Tuple[int, int]:
    '''Stage 3: Battle, Phase 2: Battle, Step 2: Battle w/ Rolls'''
    num_rolls_att: int = (att_player.contr_states[state_att] - 1
                          if att_player.contr_states[state_att] < 4
                          else 3)

    num_rolls_def: int = (2 if def_player.contr_states[state_def] > 1
                          else 1)
    att_rolls: List[int] = battle_rolls(num_rolls_att)
    def_rolls: List[int] = battle_rolls(num_rolls_def)

    print(att_rolls)
    print(def_rolls)
    print(att_player.contr_states)
    print(def_player.contr_states)

    return battle_roll_loss(att_rolls, def_rolls)


def battle_move_troop_step(att_player: Player, att_ind, def_ind: int) -> None:
    '''Stage 3: Battle, Phase 2: Battle, Step 3: Move Troops if possible'''
    att_troop_num: int = att_player.contr_states[att_ind]
    print(f'Enter the number of troops you want to move ' +
          f'[1-{att_troop_num-1}]: ')

    num_moved: int = int(input())
    if num_moved < 1 or num_moved > att_troop_num - 1:
        num_moved = int(input())

    att_player.contr_states[att_ind] -= num_moved
    att_player.contr_states[def_ind] += num_moved


class Board:
    '''Declaration of Board Class'''
    def __init__(self,
                 *args,
                 **kwargs: Dict[str, Any]) -> None:
        self.players: List[Player] = []
        self.curr_stage: int = 0
        self.count_troops: List[int] = [0] * NUM_COUNTRIES
        self.player_turn: int = 0

        if 'num_players' in kwargs or args != ():
            # Has num_players
            num_players: int = 0
            if args != ():
                num_players = args[0]
            else:
                num_players = safe_input(kwargs, 'num_players', int)

            for _ in range(num_players):
                self.players.append(Player())
        else:
            # Fill in values
            self.players = safe_input(kwargs, 'players', list)
            self.curr_stage = safe_input(kwargs, 'curr_stage', int)
            self.count_troops = safe_input(kwargs, 'count_troops', int)
            self.player_turn = safe_input(kwargs, 'player_turn', int)

    # Note: Currently assumes
    def set_board(self) -> None:
        '''Stage 1: Placing Troops'''
        print()
        print(self.count_troops)
        print(f'Player {self.player_turn} countr. num: ')

        new_count: int = int(input())
        while (not within_range(new_count)
               or self.count_troops[new_count] != 0):
            new_count = int(input())

        self.players[self.player_turn].contr_states[new_count] = 1
        self.count_troops[new_count] = 1

        if 0 not in self.count_troops:
            self.curr_stage += 1
            self.player_turn = len(self.players) - 1

    def reinf_count(self) -> None:
        '''Stage 2: Fortifying Troops'''
        print()
        print(self.players[self.player_turn].contr_states)

        contin_stage: bool = functools.reduce(
            lambda a, b: a or b,
            [pl.get_count() <= 25 for pl in self.players])

        if not contin_stage:
            self.curr_stage += 1
            self.player_turn = len(self.players) - 1

        if self.players[self.player_turn].get_count() >= 25:
            return

        print(f'Player {self.player_turn} countr. num: ')

        new_count: int = int(input())
        while (not within_range(new_count)
               or self.players[self.player_turn].contr_states[new_count] == 0):
            new_count = int(input())

        self.players[self.player_turn].contr_states[new_count] += 1

    def get_def_player(self, def_ind: int) -> Player:
        '''Find player associated with country'''
        def_pl_ind: int = [1 if player.contr_states[def_ind] > 0 else 0
                           for player in self.players].index(1)
        return self.players[def_pl_ind]

    def battle(self) -> None:
        '''Stage 3: Normal Battling'''
        att_player: Player = self.players[self.player_turn]

        print()
        print('BATTLE')
        print(f'Player {self.player_turn}: ')
        print(att_player.contr_states)

        # Phase 1: Fortify Troops
        battle_fort_phase(att_player, reinf_num(att_player))

        # Phase 2: Battle
        print('BATTLE PHASE')
        while True:
            print('Attack?')
            if int(input()) == 0:
                break

            # Step 1: Select Countries
            print('Enter Attacking State & Defending State: ')
            is_valid, state_att, state_def = battle_sel_count_step(
                att_player.contr_states,
                int(input()),
                int(input()))

            if not is_valid:
                continue

            # Find player associated with country
            def_player: Player = self.get_def_player(state_def)

            # Step 2: Battle w/ Rolls
            num_att_loss, num_def_loss = battle_battle_step(att_player,
                                                            def_player,
                                                            state_att,
                                                            state_def)

            # Step 3: Battle Consequences
            att_player.contr_states[state_att] -= num_att_loss
            def_player.contr_states[state_def] -= num_def_loss

            if def_player.contr_states[state_def] == 0:
                battle_move_troop_step(att_player, state_att, state_def)

            if def_player.get_count() == 0:
                def_player.is_alive = False

        # TODO: Give option to move troops
        # TODO: Receive Card if possible

    def turn(self) -> None:
        '''Method Executing Turn Based on Stage Num'''
        stages: Dict[int, Callable[[], None]] = {
            0: self.set_board,
            1: self.reinf_count,
            2: self.battle
        }

        stages[self.curr_stage]()
        self.player_turn = (self.player_turn + 1) % len(self.players)

    def winner(self) -> int:
        '''Write Function to Determine if there is a winner'''
        num_alive: int = 0
        ind_alive: int = -1

        for i, player in enumerate(self.players):
            if player.is_alive:
                num_alive += 1
                ind_alive = i

        if num_alive == 1:
            return ind_alive

        return -1

    def game(self) -> int:
        '''Function that plays the full game of Risk and returns the winner'''
        winner: int = -1

        while self.curr_stage != 3 or winner == -1:
            self.turn()
            winner = self.winner()

        return winner
