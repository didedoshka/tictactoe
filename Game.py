from tictactoe.State import State
from copy import deepcopy


def correct_moves(state: State) -> list[tuple[int, str]]:
    moves = []
    for i in range(9):
        if state.board[i] == '.':
            moves.append((i, state.turn))
    return moves

def move(state: State, move: tuple[int, int]):
    new_state = deepcopy(state)
    new_state.board[move[0]] = 'x' if move[1] == 0 else 'o'
    terminated = did_end(new_state)
    if terminated is not None:
        new_state.terminated = terminated
    new_state.turn = 1 - state.turn
    reward = ((None, 0),)
    if terminated == 'x':
        reward = ((0, 2),)
    elif terminated == 'o':
        reward = ((1, 2),)
    elif terminated == 'd':
        # reward = (, 1)
        reward = ((0, 1), (1, 1))
    return new_state, reward


def did_win(state: State, symbol: str):
    if state.board[0] == state.board[1] == state.board[2] == symbol:
        return True
    if state.board[3] == state.board[4] == state.board[5] == symbol:
        return True
    if state.board[6] == state.board[7] == state.board[8] == symbol:
        return True
    if state.board[0] == state.board[3] == state.board[6] == symbol:
        return True
    if state.board[1] == state.board[4] == state.board[7] == symbol:
        return True
    if state.board[2] == state.board[5] == state.board[8] == symbol:
        return True
    if state.board[0] == state.board[4] == state.board[8] == symbol:
        return True
    if state.board[2] == state.board[4] == state.board[6] == symbol:
        return True
    return False


def did_draw(state: State):
    for symbol in state.board:
        if symbol == '.':
            return False
    return True


def did_end(state: State):
    if did_win(state, 'x'):
        return 'x'
    if did_win(state, 'o'):
        return 'o'
    if did_draw(state):
        return 'd'
