import textwrap


class State:

    number_of_players = 2

    def __init__(self) -> None:
        self.board: list[str] = ['.'] * 9
        self.turn: int = 0
        self.terminated: str | None = None

    def get_ansi(self):
        return textwrap.dedent(f'''
            {self.board[0]}|{self.board[1]}|{self.board[2]}
            -----
            {self.board[3]}|{self.board[4]}|{self.board[5]}
            -----
            {self.board[6]}|{self.board[7]}|{self.board[8]}
            ''')

    def get_minimal_ansi(self):
        return textwrap.dedent(f'''
            {self.board[0]}{self.board[1]}{self.board[2]}
            {self.board[3]}{self.board[4]}{self.board[5]}
            {self.board[6]}{self.board[7]}{self.board[8]}
            ''')

    def __hash__(self) -> int:
        h = 0
        for i in range(9):
            if self.board[i] == '.':
                h += 1 * 10**i
            elif self.board[i] == 'x':
                h += 2 * 10**i
            else:
                h += 3 * 10**i
        return h
