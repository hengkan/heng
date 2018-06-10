"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
import copy
from stack import Stack
from tree import Tree


def interactive_strategy(game: 'Game') -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: 'Game') -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def all_possible_state(game: 'Game') -> list:
    """
    Return a list of all possible games whose current states are possibly
    derived from game.
    """
    b = []
    c = game.current_state.get_possible_moves()
    for move in c:
        d = copy.copy(game)
        d.current_state = game.current_state.make_move(move)
        b.append(d)
    return b


def recursive_score(game: 'Game') -> int:
    """
    Return a minimax score for the game using recursion.
    """
    if game.is_over(game.current_state) is True:
        if game.is_winner(game.current_state.get_current_player_name()):
            return 1
        elif game.is_winner('p1') is False and game.is_winner('p2') is False:
            return 0
        return -1
    return max([-1 * recursive_score(x) for x in all_possible_state(game)])


def recursive_minimax(game: 'Game') -> Any:
    """
    Return a minimax move for the game using recursion.
    """
    if game.is_over(game.current_state) is True:
        return None
    c = [recursive_score(x) for x in all_possible_state(game)]
    d = min(c)
    e = c.index(d)
    return game.current_state.get_possible_moves()[e]


def score(game: 'Game') -> int:
    """
    Return an integer representation to show the winner

    Precondition; game.is_over(game.current_state)
    """
    if game.is_winner(game.current_state.get_current_player_name()):
        return 1
    elif game.is_winner('p1') is False and game.is_winner('p2') is False:
        return 0
    return -1


def iterative_minimax(game: 'Game') -> Any:
    """
    Return a minimax move for the game using iteration.
    """
    if game.is_over(game.current_state) is True:
        return None
    a = Stack()
    b = Tree(game.current_state)
    a.add(b)
    while a.is_empty() is False:
        c = a.remove()
        if game.is_over(c.value) is True:
            game1 = copy.copy(game)
            game1.current_state = c.value
            c.score = score(game1)
        elif c.children == []:
            m = c.value.get_possible_moves()
            states = [c.value.make_move(move) for move in m]
            trees = [Tree(state) for state in states]
            c.children = trees
            a.add(c)
            for tree in c.children:
                a.add(tree)
        else:
            empty = []
            for tree in c.children:
                empty.append(-1 * tree.score)
            c.score = max(empty)
    h = [tree.score for tree in c.children]
    mini = min(h)
    minindex = h.index(mini)
    return c.value.get_possible_moves()[minindex]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
