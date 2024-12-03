import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button Example")

# Define button properties
button_color = (0, 255, 0)  # Green
hover_color = (0, 200, 0)  # Darker green
text_color = (255, 255, 255)  # White
button_rect = pygame.Rect(300, 250, 200, 50)  # x, y, width, height

# Set up the font
font = pygame.font.Font(None, 36)
button_text = font.render("Click Me!", True, text_color)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Check if clicked inside button
                print("Button clicked!")

    # Fill the screen with a background color
    screen.fill((0, 0, 0))  # Black background

    # Check for mouse hover
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color

    # Draw the button
    pygame.draw.rect(screen, color, button_rect)

    # Center the text on the button
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()