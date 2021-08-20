import pygame
import player
import game_functions

# Initialize the pygame.
pygame.init()

# Create the screen (800x800 pixels).
screen = pygame.display.set_mode((800, 800))

# Setting background.
background = pygame.image.load('img/background.jpg')
# Setting background music, infinite play.
pygame.mixer.music.load("music/background.wav")
pygame.mixer.music.play(-1)

# Setting icon for a program and also it's name.
pygame.display.set_caption("Space Ship")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)


# Creating player
player = player.Player()


# Game Loop
running = True
while running:
    # Adding background image to the screen
    screen.blit(background, (0, 0))

    # Checking for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.set_player_X_change(-5)
            if event.key == pygame.K_RIGHT:
                player.set_player_X_change(5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.set_player_X_change(0)

    # Player movement
    player.player_move()


    game_functions.draw_player(screen,player)
    pygame.display.update()

# Quiting Pygame
pygame.quit()