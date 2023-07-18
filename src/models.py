import random


class BoardClass:
    def __init__(self, width: int = 50, height: int = 50, move: int = 0, board: list[list[int]] | None = None):
        self.width = width
        self.height = height
        self.move = move
        if board is not None:
            self.board = board
        else:
            self.board = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

    @staticmethod
    def cell_next_state(x: int, y: int, board: list[list], is_dead: bool) -> int:
        """ Defines state of a single cell"""
        if is_dead:
            if sum(sum(board[z][x - 1:x + 2]) for z in range(y - 1, y + 2)) == 3:
                return 1
            return 0
        else:
            if sum(sum(board[z][x - 1:x + 2]) for z in range(y - 1, y + 2)) in (3, 4):
                return 1
            return 0

    def update_board(self):
        """ Updates state of the board"""
        new_board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for row in range(-1, self.height - 1):
            for column in range(-1, self.width - 1):
                if self.board[row][column] == 1:
                    """ Alive cell"""
                    new_board[row][column] = self.cell_next_state(x=column, y=row, board=self.board, is_dead=False)
                else:
                    """ Dead cell"""
                    new_board[row][column] = self.cell_next_state(x=column, y=row, board=self.board, is_dead=True)
        self.board = new_board
        self.move += 1

    def game_over(self, data) -> bool:
        """ Checks if current state of the board matches latest states"""
        for key in data:
            if self.board == data[key]["board"]:
                return True
        return False
