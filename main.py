import pygame
import sys
from oop_cell_board import *
# imported all the previous code and initiate pygame
pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((width, height))
screen_color = white
line_color = black
screen.fill(white)
number_font = pygame.font.Font(None, num_size)
button_font = pygame.font.Font(None, butt_size)
text_font = pygame.font.Font(None, menu_size)
pygame.display.update()
game_over = False
game_start = False


def draw_game_over_won():
    screen.fill(screen_color)
    end_text = "Game Over! You won!"
    end_surf = text_font.render(end_text, True, black)
    end_rect = end_surf.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(end_surf, end_rect)
    # exit button
    exit_text = button_font.render("Exit", True, white)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(black)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(3 * (width // 4), height // 2 + 235))
    screen.blit(exit_surface, exit_rectangle)


def draw_game_over_lost():
    end_text = "Game Over! You filled out the wrong numbers!"
    end_surf = text_font.render(end_text, True, black)
    end_rect = end_surf.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(end_surf, end_rect)
    # restart button
    restart_text = button_font.render("Restart", True, white)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(black)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(width // 2, height // 2 + 235))
    screen.blit(restart_surface, restart_rectangle)


def draw_start_game():
    screen.fill(screen_color)
    # top text
    top_text = "Welcome to Sudoku!"
    top_surf = number_font.render(top_text, True, red)
    top_rect = top_surf.get_rect(center=(width // 2, height // 2 - 220))
    screen.blit(top_surf, top_rect)
    # middle text
    mid_text = "Select Game Mode:"
    mid_surf = number_font.render(mid_text, True, red)
    mid_rect = mid_surf.get_rect(center=(width // 2, height // 2 - 110))
    screen.blit(mid_surf, mid_rect)
    # add buttons for easy medium and difficult - maybe add user criteria to pull the func to take out the values
    # Initialize buttons
    # button text
    easy_text = button_font.render("Easy", True, white)
    med_text = button_font.render("Medium", True, white)
    hard_text = button_font.render("Hard", True, white)

    # Initialize button background color and text
    # easy
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(red)
    easy_surface.blit(easy_text, (10, 10))
    # med
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(red)
    med_surface.blit(med_text, (10, 10))
    # hard
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(red)
    hard_surface.blit(hard_text, (10, 10))
    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(width // 2, height // 2 + 50))
    med_rectangle = med_surface.get_rect(
        center=(width // 2, height // 2 + 125))
    hard_rectangle = hard_surface.get_rect(
        center=(width // 2, height // 2 + 200))
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    return difficulty
                elif med_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    return difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    return difficulty
        pygame.display.update()





    # need buttons for:
    # • The Reset button will reset the board to its initial state.
    # • The Restart button will take the user back to the Game Start screen.
    # • The Exit button will end the program.
    # button text
reset_text = button_font.render("Reset", True, white)
restart_text = button_font.render("Restart", True, white)
exit_text = button_font.render("Exit", True, white)
    # Initialize button background color and text
    # reset
reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
reset_surface.fill(black)
reset_surface.blit(reset_text, (10, 10))
    # restart
restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
restart_surface.fill(black)
restart_surface.blit(restart_text, (10, 10))
    # exit
exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
exit_surface.fill(black)
exit_surface.blit(exit_text, (10, 10))
    # Initialize button rectangle
reset_rectangle = reset_surface.get_rect(
    center=(width // 4, height // 2 + 235))
restart_rectangle = restart_surface.get_rect(
    center=(2 * (width // 4), height // 2 + 235))
exit_rectangle = exit_surface.get_rect(
    center=(3 * (width // 4), height // 2 + 235))
    # Draw buttons


def print_butt():
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

def win_or_lose():
    if sud_board.check_board() is True:
        screen.fill(white)
        draw_game_over_won()
        pygame.display.update()
    elif sud_board.check_board() is False:
        screen.fill(white)
        draw_game_over_lost()
        pygame.display.update()


while True:
    if game_start is False:
        pygame.display.update()
        pygame.time.delay(1000)
        difficulty = draw_start_game()
        # figure out how to do if they click easy, med and hard buttons
        # when those are clicked game_start is True
    # event loop

        sud_board = Board(width, height, screen, difficulty)
        game_start = True
        game_over = False
        screen.fill(white)
        pygame.display.update()
        sud_board.draw()
        print_butt()
        pygame.display.update()
    for event in pygame.event.get():
        if sud_board.is_full() and sud_board.sketched is False:
            if sud_board.check_board():
                screen.fill(white)
                draw_game_over_won()
                pygame.display.update()
            else:
                screen.fill(white)
                draw_game_over_lost()
                pygame.display.update()
        if event.type == pygame.QUIT: # exit button?
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rectangle.collidepoint(event.pos):
                sys.exit()
            elif reset_rectangle.collidepoint(event.pos):
                sud_board.reset_to_original()
                screen.fill(white)
                sud_board.draw()
                print_butt()
                pygame.display.update()
            elif restart_rectangle.collidepoint(event.pos):
                screen.fill(white)
                game_start = False
                game_over = True
                continue
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            click_pos = pygame.mouse.get_pos()
            x, y = click_pos
            row = y // square_size
            col = x // square_size
            sud_board.select(row, col)
            # if selected and empty let user place value
        if event.type == pygame.KEYDOWN and not game_over:
            if sud_board.select:
                if event.key == pygame.K_1:
                    sud_board.sketch(1)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_2:
                    sud_board.sketch(2)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_3:
                    sud_board.sketch(3)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_4:
                    sud_board.sketch(4)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_5:
                    sud_board.sketch(5)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_6:
                    sud_board.sketch(6)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_7:
                    sud_board.sketch(7)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_8:
                    sud_board.sketch(8)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_9:
                    sud_board.sketch(9)
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_TAB:
                    sud_board.place_number(sud_board.board[sud_board.selected_cell[0]][sud_board.selected_cell[1]])
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()
                if event.key == pygame.K_0:
                    sud_board.clear()
                    screen.fill(white)
                    sud_board.draw()
                    print_butt()
                    pygame.display.update()