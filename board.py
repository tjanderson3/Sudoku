import pygame
from sudoku_generator import *
from constants import *
from cell import Cell
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen  # screen is a window from PyGame
        self.difficulty = difficulty
        if difficulty == 'easy':
            self.board = generate_sudoku(9, 30)
            edit_cells = []
            for k in range(9):
                for l in range(9):
                    if self.board[k][l] == 0:
                        edit_cells.append(tuple((k, l)))
        elif difficulty == 'medium':
            self.board = generate_sudoku(9, 40)
            edit_cells = []
            for k in range(9):
                for l in range(9):
                    if self.board[k][l] == 0:
                        edit_cells.append(tuple((k, l)))
        elif difficulty == 'hard':
            self.board = generate_sudoku(9, 50)
            edit_cells = []
            for k in range(9):
                for l in range(9):
                    if self.board[k][l] == 0:
                        edit_cells.append(tuple((k, l)))
        # difficulty is a variable to indicate if a user chose easy, medium, or hard

        self.cells = [
            [Cell(self.board[i][j], i, j, square_size) for j in range(9)]
            for i in range(9)
        ]

    def draw(self):
        # draws an outline of the Sudoku grid with bold lines to delineate the 3 X 3 boxes
        # draws every cell on this board
        for i in range(1, board_rows + 1):#thick and thin horizontal lines
            pygame.draw.line(
                self.screen,
                black,
                (0, i * square_size),
                (width, i * square_size),
                thinner_line
            )
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    black,
                    (0, i * square_size),
                    (width, i * square_size),
                    thicker_line
                )
        # draw vertical lines
        for j in range(1, board_cols):
            pygame.draw.line(
                self.screen,
                black,
                (j * square_size, 0),
                (j * square_size, width),
                thinner_line
            )
            if j % 3 == 0:
                pygame.draw.line(
                    self.screen,
                    black,
                    (j * square_size, 0),
                    (j * square_size, width),
                    thicker_line
                )
        """for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()"""

    def select(self, row, col):
        # may need to loop thru and make sure you're deselecting previous by looping through every cell and making sure its false
        #call in main "mouse button down"
        self.cells[row][col].selected = True

    def click(self, x, y):
        if self.select(x, y):
            tuple = (x, y)
            return tuple



    def clear(self):
        if self.select:
            pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        Cell.draw()
        pass

    def reset_to_original(self):
        for cell in self.board:
            pass

    def is_full(self):
        count = self.height * self.width  # number of spaces on the board
        for i in range(self.height):
            for j in range(self.width):
                # nested for loop to check all the spaces on the board
                if self.board[i][j] != 0:
                    count -= 1
        if count == 0:  # if all spaces full return True
            return True
        else:
            return False

    def update_board(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height // self.width,
                            self.width // self.height) for j in range(self.height)] for i in range(self.width)]

    def find_empty(self):
        for i in range(self.height):
            for j in range(self.width):
                # for loop to go through all the spaces in the board
                if not self.board[i][j] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                    empty_location = (i, j)
                    return empty_location
        return None

    def check_board(self):
        SudokuGenerator.is_valid(self.row, self.col, self.num)
        # does this call all of the if valids separately?

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return  # If the mouse is on the start button, we can return to
main
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()