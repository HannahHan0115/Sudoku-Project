import pygame
#im still figuring out pygame - Ben
def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((900, 1000))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light blue")
            for row in range(0,9):
                if row%3==0:
                    pygame.draw.line(screen, "black", (0, 100*row), (900, 100*row) )
                else:
                    pygame.draw.line(screen, "gray", (0, 100 * row), (900, 100 * row))
            for row in range(0,9):
                if row%3==0:
                    pygame.draw.line(screen, "black", (0, 100*row), (900, 100*row) )
                else:
                    pygame.draw.line(screen, "gray", (0, 100 * row), (900, 100 * row))
            pygame.display.update()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()