"""
An implementation of a state for Stonehenge
An implementation of a game for Stonehenge

"""
from typing import Any
import copy
from game_state import GameState
from game import Game


A = {(1, 1): 'AA', (1, 2): 'BB', (2, 1): 'CC'}
B = ({(1, 1): 'AA', (1, 2): 'BB', (2, 1): 'CC', (2, 2): 'DD',
      (2, 3): 'EE', (3, 1): 'FF', (3, 2): 'GG'})
C = ({(1, 1): 'AA', (1, 2): 'BB', (2, 1): 'CC', (2, 2): 'DD',
      (2, 3): 'EE', (3, 1): 'FF', (3, 2): 'GG', (3, 3): 'HH',
      (3, 4): 'II', (4, 1): 'JJ', (4, 2): 'KK', (4, 3): 'LL'})
D = ({(1, 1): 'AA', (1, 2): 'BB', (2, 1): 'CC', (2, 2): 'DD',
      (2, 3): 'EE', (3, 1): 'FF', (3, 2): 'GG', (3, 3): 'HH',
      (3, 4): 'II', (4, 1): 'JJ', (4, 2): 'KK', (4, 3): 'LL',
      (4, 4): 'MM', (4, 5): 'NN', (5, 1): '0O', (5, 2): 'PP',
      (5, 3): 'QQ', (5, 4): 'RR'})
E = ({(1, 1): 'AA', (1, 2): 'BB', (2, 1): 'CC', (2, 2): 'DD',
      (2, 3): 'EE', (3, 1): 'FF', (3, 2): 'GG', (3, 3): 'HH',
      (3, 4): 'II', (4, 1): 'JJ', (4, 2): 'KK', (4, 3): 'LL',
      (4, 4): 'MM', (4, 5): 'NN', (5, 1): '0O', (5, 2): 'PP',
      (5, 3): 'QQ', (5, 4): 'RR', (5, 5): 'SS', (5, 6): 'TT',
      (6, 1): 'UU', (6, 2): 'VV', (6, 3): 'WW', (6, 4): 'XX',
      (6, 5): 'YY'})
F = ({'A-B': '@', 'C': '@', 'A': '@', 'B-C': '@', 'A-C': '@',
      'B': '@'})
G = ({'A-B': '@', 'C-D-E': '@', 'F-G': '@', 'A-C': '@',
      'B-D-F': '@', 'E-G': '@', 'C-F': '@', 'A-D-G': '@',
      'B-E': '@'})
H = ({'A-B': '@', 'C-D-E': '@', 'F-G-H-I': '@', 'J-K-L': '@',
      'A-C-F': '@', 'B-D-G-J': '@', 'E-H-K': '@',
      'I-L': '@', 'F-J': '@', 'C-G-K': '@', 'A-D-H-L': '@',
      'B-E-I': '@'})
K = ({'A-B': '@', 'C-D-E': '@', 'F-G-H-I': '@', 'J-K-L-M-N': '@',
      'O-P-Q-R': '@', 'A-C-F-J': '@', 'B-D-G-K-O': '@',
      'E-H-L-P': '@', 'I-M-Q': '@', 'N-R': '@', 'J-O': '@',
      'F-K-P': '@', 'C-G-L-Q': '@', 'A-D-H-M-R': '@',
      'B-E-I-N': '@'})
J = ({'A-B': '@', 'C-D-E': '@', 'F-G-H-I': '@', 'J-K-L-M-N': '@',
      'O-P-Q-R-S-T': '@', 'U-V-W-X-Y': '@', 'A-C-F-J-O': '@',
      'B-D-G-K-P-U': '@', 'E-H-L-Q-V': '@', 'I-M-R-W': '@',
      'N-S-X': '@', 'T-Y': '@', 'O-U': '@',
      'J-P-V': '@', 'F-K-Q-W': '@', 'C-G-L-R-X': '@',
      'A-D-H-M-S-Y': '@', 'B-E-I-N-T': '@'})


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.

    length_side:  the length side of the game  - length side is less than 6
    cell: the record of cells for the game
    ley_line: the record of ley_lines for the game
    """
    length_side: int
    cell: dict
    ley_line: dict

    def __init__(self, is_p1_turn: bool, n: int) -> None:
        """
        Initialize this game state based on is_p1_turn and n
        """
        GameState.__init__(self, is_p1_turn)
        self.length_side = n
        if n == 1:
            self.cell = A
            self.ley_line = F
        elif n == 2:
            self.cell = B
            self.ley_line = G
        elif n == 3:
            self.cell = C
            self.ley_line = H
        elif n == 4:
            self.cell = D
            self.ley_line = K
        else:
            self.cell = E
            self.ley_line = J

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game .
        """
        i = 1
        a = self.cell
        b = self.ley_line
        n = self.length_side
        e = ''
        e = (e + " " * (2 * n + 4) + "{}   {}".format
             (b[list(b.keys())[n + 1]], b[list(b.keys())[n + 2]]) + '\n')
        e = e + " " * (2 * n + 3) + "/   /" + '\n'
        while i != n:
            t = 2 * i + 3
            c = (e + ' ' * (2 * n - 2 * i) +
                 "{}".format(b[list(b.keys())[i - 1]]))
            for j in range(1, i + 2):
                c += " - {}".format(a[(i, j)][1])
            c += "   {}".format(b[list(b.keys())[n + 2 + i]]) + '\n'
            c += ' ' * (2 * n - 2 * i + 3)
            for h in range(t, 0, -1):
                c += '/ ' if h % 2 == 1 else '\\ '
            c += '\n'
            e = c
            i += 1
        e += "{}".format(b[list(b.keys())[n - 1]])
        for m in range(1, n + 2):
            e += ' - {}'.format(a[(n, m)][1])
        e += '\n'
        e += ' ' * 5
        for v in range(2 * n + 1, 0, -1):
            e += '\\ ' if v % 2 == 1 else '/ '
        e += '\n'
        e += ' ' * 2 + "{}".format(b[list(b.keys())[n]])
        for l in range(1, n + 1):
            e += " - {}".format(a[(n + 1, l)][1])
        e += '   {}'.format(b[list(b.keys())[-1]]) + '\n'
        e += ' ' * 7
        t = 1
        while t != n + 1:
            e += '\\   '
            t += 1
        e += '\n' + ' ' * 8
        for k in range(- n - 1, -1):
            e += '{}   '.format(b[list(b.keys())[k]])
        return e

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        moves = []
        c = len(self.ley_line)
        a = list(self.ley_line.values()).count('1')
        b = list(self.ley_line.values()).count('2')
        for item in self.cell:
            if (self.cell[item][1] != '1' and self.cell[item][1] != '2')\
                    and (a < 0.5 * c and b < 0.5 * c):
                moves.append(self.cell[item][0])
        return moves

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def make_move(self, move: Any) -> "StonehengeState":
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_cell = copy.copy(self.cell)
        new_ley_line = copy.copy(self.ley_line)
        for item in new_cell:
            if new_cell[item][1] == move:
                a = new_cell[item][0]
                new_cell[item] = a + self.get_current_player_name()[1]
        for item in new_ley_line:
            h = [s for s in item if s != '-']
            total = 0
            for cap in h:
                capn = cap + self.get_current_player_name()[1]
                total = total + 1 if capn in list(new_cell.values()) else total
            d = 0.5 * len(h)
            if total >= d and move in item and new_ley_line[item] == '@':
                new_ley_line[item] = self.get_current_player_name()[1]
        new_state = StonehengeState(not self.p1_turn, self.length_side)
        new_state.cell = new_cell
        new_state.ley_line = new_ley_line
        return new_state

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        a = ("p1's turn:{}, length side:{}, cells:{}, ley lines:{}".format
             (self.p1_turn, self.length_side, self.cell, self.ley_line))
        return a

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        name = self.get_current_player_name()[1]
        for move in self.get_possible_moves():
            total = 0
            c = self.make_move(move).ley_line
            for item in c:
                total = total + 1 if c[item] == name else total
            if total >= 0.5 * len(c):
                return self.WIN
        h = [self.make_move(move) for move in self.get_possible_moves()]
        for state in h:
            m = state.get_possible_moves()
            n = [state.make_move(t).ley_line for t in m]
            boo = any([list(a.values()).count(state.get_current_player_name()
                                              [1]) >= 0.5 * len(a) for a in n])
            if boo is False:
                return self.DRAW
        return self.LOSE


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.

    current_state: the current state for the game
    """
    current_state: "StonehengeState"

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        count = int(input("Enter the number of length side :"))
        self.current_state = StonehengeState(p1_starts, count)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = "Players take turns claiming cells to capture" + \
            " at least half of cells in a ley-line in order to" + \
            " capture a ley-line. The first one who captures" + \
            " at least half of the ley-lines is the winner."
        return instructions

    def is_over(self, state: 'StonehengeState') -> bool:
        """
        Return whether or not this game is over according to state.
        """
        d = state.ley_line
        return (list(d.values()).count('1') >= 0.5 * len(d) or
                list(d.values()).count('2') >= 0.5 * len(d) or
                state.get_possible_moves() == [])

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.
        """
        if not string.strip().isupper() or len(string.strip()) != 1:
            return 'INVALID'
        return string.strip()



if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
