import pygame
from constants import *
from sudoku_generator import *


"""class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = False
        self.draw_font = num_size
        self.selected = False

    def set_cell_value(self, value):
        # sets the value in the center of the cell
        self.value = value

    def set_sketched_value(self, value):
        # sets the sketched inputted value in the top left of the cell, light gray
        self.sketch = value

    def draw(self, screen):
        val_font = pygame.font.Font(None, self.draw_font)
        if self.sketch is True:
            color = gray
            location = (square_size * self.col + 10, square_size * self.row + square_size + 10)
        else:
            color = black
            location = (square_size * self.col + square_size // 2, square_size * self.row + square_size // 2)
        val_surf = val_font.render(self.value, True, color)
        if self.value != 0:
            val_rect = val_surf.get_rect(center=location)
            self.screen.blit(val_surf, val_rect)

        if self.selected is True:  # make red
            for i in range(2):
                pygame.draw.rect(
                    screen,
                    red,
                    (square_size, square_size),
                    thicker_line
                )"""

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen  # screen is a window from PyGame
        self.difficulty = difficulty
        self.selected_cell = None
        self.sketched = False
        if difficulty == 30:
            self.board = generate_sudoku(9, 30)
        elif difficulty == 40:
            self.board = generate_sudoku(9, 40)
        elif difficulty == 50:
            self.board = generate_sudoku(9, 50)
        self.edit_cells = []
        for k in range(9):
            for l in range(9):
                if self.board[k][l] == 0:
                    self.edit_cells.append(tuple((k, l)))


    def draw(self):
        for i in range(1, board_rows + 1):  # thick and thin horizontal lines
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
        val_font = pygame.font.Font(None, 40)
        for i in range(9):
            for j in range(9):
                if self.sketched is True and i == self.selected_cell[0] and j == self.selected_cell[1]:
                    color = gray
                    loc = (square_size * j + 15, square_size * i + square_size - 40)
                    val_surf = val_font.render(str(self.board[i][j]), True, color)
                    if self.board[i][j] != 0:
                        val_rect = val_surf.get_rect(center=loc)
                        self.screen.blit(val_surf, val_rect)
                else:
                    color = black
                    loc = (square_size * j + square_size // 2, square_size * i + square_size // 2)
                    val_surf = val_font.render(str(self.board[i][j]), True, color)
                    if self.board[i][j] != 0:
                        val_rect = val_surf.get_rect(center=loc)
                        self.screen.blit(val_surf, val_rect)

    def select(self, row, col):
        # may need to loop thru and make sure ur deselecting prev by looping thru every cell and making sure its false
        # call in main "mouse button down"
        self.selected_cell = (row, col)

    def clear(self):
        if self.selected_cell in self.edit_cells:
            self.board[self.selected_cell[0]][self.selected_cell[1]] = 0

    def sketch(self, value):
        self.sketched = True
        if self.selected_cell in self.edit_cells:
            self.board[self.selected_cell[0]][self.selected_cell[1]] = value

    # sketch = True use that color and then use
    # click value to make the cell in that box sketched then call draw in cell to place the value

    def place_number(self, value):
        # call cell draw to place value, sketched is = false which is default
        self.sketched = False
        if self.selected_cell in self.edit_cells:
            self.board[self.selected_cell[0]][self.selected_cell[1]] = value


    def reset_to_original(self):
        for tup in self.edit_cells:
            self.board[tup[0]][tup[1]] = 0


    def is_full(self):
        count = 81  # number of spaces on the board
        for i in range(9):
            for j in range(9):
                # nested for loop to check all the spaces on the board
                if self.board[i][j] != 0:
                    count -= 1
        if count == 0:  # if all spaces full return True
            return True
        else:
            return False

    def find_empty(self):
        for i in range(self.height):
            for j in range(self.width):
                # for loop to go through all the spaces in the board
                if not self.board[i][j] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                    empty_location = (i, j)
                    return empty_location
        return None

    def check_board(self):
        for i in range(9):
            row_vals = []
            for j in range(9):
                row_vals.append(self.board[i][j])
                if j == 8:
                    if len(row_vals) != len(set(row_vals)) and 0 not in row_vals:
                        return False
        for j in range(9):
            col_vals = []
            for i in range(9):
                col_vals.append(self.board[i][j])
                if i == 8:
                    if len(col_vals) != len(set(col_vals)) and 0 not in col_vals:
                        return False
        for i in range(0, 9, 3):
            box_vals = []
            for j in range(3):
                box_vals.append(self.board[i][j])
                if j == 2:
                    if len(box_vals) != len(set(box_vals)) and 0 not in box_vals:
                        return False
        for j in range(0, 9, 3):
            box_vals = []
            for i in range(3):
                box_vals.append(self.board[i][j])
                if i == 2:
                    if len(box_vals) != len(set(box_vals)):
                        return False
        return True








