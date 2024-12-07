import pygame
import sudoku_generator
import Cell
import Board

def draw_start_screen(screen):
    screen.fill("white")
    start_title_font = pygame.font.Font(None, 75)
    game_mode_font = pygame.font.Font(None, 50)
    difficulty_font = pygame.font.Font(None, 50)

    text_surface = start_title_font.render("Welcome to Sudoku", True, "Black")
    title_rectangle = text_surface.get_rect(center = (720/2, 800/2-300))
    screen.blit(text_surface, title_rectangle)

    game_mode_surface = game_mode_font.render("Select Game Mode:", True, "Black")
    game_mode_rectangle = game_mode_surface.get_rect(center=(720/2, 800/2-150))
    screen.blit(game_mode_surface, game_mode_rectangle)

    easy_text = difficulty_font.render("EASY", True, "white")
    medium_text = difficulty_font.render("MEDIUM", True, "white")
    hard_text = difficulty_font.render("HARD", True, "white")
    #making the orange rectangle
    easy_surface = pygame.Surface((easy_text.get_size()[0]+20, easy_text.get_size()[1]+20))
    easy_surface.fill("Orange")
    easy_surface.blit(easy_text, (10, 10))
    easy_surface_rectangle = easy_surface.get_rect(center=(720/4, 800/2))
    screen.blit(easy_surface, easy_surface_rectangle)

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill("Orange")
    medium_surface.blit(medium_text, (10, 10))
    medium_surface_rectangle = medium_surface.get_rect(center=(720/4*2, 800/2))
    screen.blit(medium_surface, medium_surface_rectangle)

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill("Orange")
    hard_surface.blit(hard_text, (10, 10))
    hard_surface_rectangle = hard_surface.get_rect(center=(720/4*3, 800/2))
    screen.blit(hard_surface, hard_surface_rectangle)

def draw_board(screen, board): #assumes that the board is (720, 800)
    screen.fill("light yellow")
    for row in range(0, 10):
        if row % 3 == 0:
            pygame.draw.line(screen, "black", (0, 80 * row), (720, 80 * row))
        else:
            pygame.draw.line(screen, "gray", (0, 80 * row), (720, 80 * row))
    for col in range(0, 9):
        if col % 3 == 0:
            pygame.draw.line(screen, "black", (80 * col, 0), (80 * col, 720))
        else:
            pygame.draw.line(screen, "gray", (80 * col, 0), (80 * col, 720))

    board_button_font = pygame.font.Font(None, 30)
    reset_text = board_button_font.render("RESET", True, "White")
    restart_text = board_button_font.render("RESTART", True, "White")
    exit_text = board_button_font.render("EXIT", True, "White")
    # making the orange rectangle
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill("Orange")
    reset_surface.blit(reset_text, (10, 10))
    reset_surface_rectangle = reset_surface.get_rect(center=(200, 760))
    screen.blit(reset_surface, reset_surface_rectangle)

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("Orange")
    restart_surface.blit(restart_text, (10, 10))
    restart_surface_rectangle = restart_surface.get_rect(center=(360, 760))
    screen.blit(restart_surface, restart_surface_rectangle)

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("Orange")
    exit_surface.blit(exit_text, (10, 10))
    exit_surface_rectangle = exit_surface.get_rect(center=(520, 760))
    screen.blit(exit_surface, exit_surface_rectangle)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                value_font = pygame.font.Font(None, 50)
                value_surface = value_font.render(str(board[i][j]), True, "Black")
                value_rectangle = value_surface.get_rect(center=(40+i*80, 40+j*80))
                screen.blit(value_surface, value_rectangle)

def draw_win_screen(screen):
    screen.fill("light green")
    win_font = pygame.font.Font(None, 100)
    win_surface = win_font.render("Game Won!", True, "Black")
    win_rectangle = win_surface.get_rect(center=(720 / 2, 800 / 2 - 250))
    screen.blit(win_surface, win_rectangle)

    exit_font = pygame.font.Font(None, 50)
    exit_text = exit_font.render("EXIT", True, "white")
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("Orange")
    exit_surface.blit(exit_text, (10, 10))
    easy_surface_rectangle = exit_surface.get_rect(center=(720 / 2, 800 / 2))
    screen.blit(exit_surface, easy_surface_rectangle)
    #print(exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20)
def draw_lose_screen(screen):
    screen.fill("crimson")
    lose_font = pygame.font.Font(None, 100)
    lose_surface = lose_font.render("Game Over :(", True, "Black")
    lose_rectangle = lose_surface.get_rect(center=(720 / 2, 800 / 2 - 250))
    screen.blit(lose_surface, lose_rectangle)

    restart_font = pygame.font.Font(None, 50)
    restart_text = restart_font.render("RESTART", True, "white")
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("Orange")
    restart_surface.blit(restart_text, (10, 10))
    easy_surface_rectangle = restart_surface.get_rect(center=(720 / 2, 800 / 2))
    screen.blit(restart_surface, easy_surface_rectangle)
    #print(restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20)
def draw_outline(row, col, screen):
    pygame.draw.rect(screen, "Red", (row*80, col*80, 80, 80), 5)
    pygame.display.update()
def remove_outline(row, col, screen):
    pygame.draw.rect(screen, "Grey", (row * 80, col * 80, 80, 80), 1)
    pygame.display.update()

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((720, 800))#this is toooooo high, when i open the game it gets out of the screen
        running = True
        # x, y, width, height
        easy_button_rect = pygame.Rect(720/4-58, 800/2-27, 116,54)
        medium_button_rect = pygame.Rect(720 / 2 - 79, 800 / 2 - 27, 158, 54)
        hard_button_rect = pygame.Rect(720 / 4*3 - 61, 800 / 2 - 27, 122, 54)
        reset_button_rect = pygame.Rect(200-42.5, 740, 85, 40)
        restart_button_rect = pygame.Rect(360-55, 740, 110, 40)
        exit_button_rect = pygame.Rect(520-39.5, 740, 69, 40)
        win_exit_button_rect = pygame.Rect(720 / 2-52, 800 / 2-27, 104, 54)
        lose_restart_button_rect = pygame.Rect(720 / 2-90, 800 / 2-27, 180, 54)
        stage=0
        #draw_lose_screen(screen)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if stage==0:#game start screen
                    draw_start_screen(screen)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if easy_button_rect.collidepoint(event.pos):  # Check if clicked inside button
                            board = sudoku_generator.generate_sudoku(9, 30)
                            #stage=1
                            stage = 1#enter the actual game screen
                        if medium_button_rect.collidepoint(event.pos):  # Check if clicked inside button
                            board = sudoku_generator.generate_sudoku(9, 40)
                            stage=1
                        if hard_button_rect.collidepoint(event.pos):  # Check if clicked inside button
                            board = sudoku_generator.generate_sudoku(9, 50)
                            stage=1
                if stage==1:
                    draw_board(screen, board)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_button_rect.collidepoint(event.pos):
                            #print('reset')
                            stage=5#it's a test
                            continue
                        if restart_button_rect.collidepoint(event.pos):
                            #print('restart')
                            stage=0
                            pygame.display.update()
                        if exit_button_rect.collidepoint(event.pos):
                            #print('exit')
                            pygame.quit()
                        if event.pos[0] <= 720 and event.pos[1] <= 720:
                            x = event.pos[0]
                            y = event.pos[1]
                            value = board[x // 80][y // 80]
                            draw_outline(x // 80, y // 80, screen)
                            stage = 6
                            continue
                            # print(event.pos[0]//80,event.pos[1]//80)#the cell it clicking

                if stage == 4:#success
                    pygame.display.update()
                    draw_win_screen(screen)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if win_exit_button_rect.collidepoint(event.pos):
                            pygame.quit()

                if stage == 5:#failed
                    pygame.display.update()
                    draw_lose_screen(screen)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if lose_restart_button_rect.collidepoint(event.pos):
                            stage=0
                            pygame.display.update()
                if stage == 6: #selecting a cell
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_button_rect.collidepoint(event.pos):
                            # print('reset')
                            stage = 5  # it's a test
                            continue
                        if restart_button_rect.collidepoint(event.pos):
                            # print('restart')
                            stage = 0
                            pygame.display.update()
                        if exit_button_rect.collidepoint(event.pos):
                            # print('exit')
                            pygame.quit()
                        remove_outline(x//80, y//80, screen)
                        x = event.pos[0]
                        y = event.pos[1]
                        value = board[x // 80][y // 80]
                        draw_outline(x // 80, y // 80, screen)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            print()
                        if event.key == pygame.K_RIGHT:
                            print()
                        if event.key == pygame.K_UP:
                            print()
                        if event.key == pygame.K_DOWN:
                            print()

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
