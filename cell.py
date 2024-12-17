import pygame
from constants import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sket_font = pygame.font.Font(None, sketched_size)
        self.selected = False
        self.sketched = 0

    def set_cell_value(self, value):
        # sets the value in the center of the cell
        self.value = value

    def set_sketched_value(self, value):
        # sets the sketched inputted value in the top left of the cell, light gray
        self.sketched = value

    def draw(self):
        # draws the cell in pygame
        num_string = str(self.value)
        num_font = pygame.font.Font(None, number_size)
        num_surf = num_font.render(num_string, 0, black)
        des_num_location = (self.row * square_size + square_size // 2, self.col * square_size + square_size // 2)
        placed_num = self.value.get_rect(center=des_num_location)
        self.screen.blit(num_surf, placed_num)
        [self.row][self.col].draw(self.screen)
        if self.selected is True:# make red
            pygame.draw.rect(
                self.screen,
                red,
                (square_size, square_size),
                thinner_line
            )
"""num_string = str(value)
        num_surf = self.num_font.render(num_string, 0, black)
        des_num_location = (self.row * square_size + square_size// 2, self.col * square_size + square_size// 2)
        placed_num = value.get_rect(center=des_num_location)
        self.screen.blit(num_surf, placed_num)sket_string = str(value)
        
        sket_string = str(value)
        sket_surf = self.sket_font.render(sket_string, 0, gray)
        des_sket_location = (self.row * square_size, self.col * square_size) # places the number in the top left
        placed_sket = value.get_rect(center=des_sket_location)
        self.screen.blit(sket_surf, placed_sket)"""