import bullet
import pygame
import game_functions
import player
import enemy

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

# Score value
score_value = 0

# Creating player
player = player.Player()
# Creating bullet
bullet = bullet.Bullet()

# Creating enemies
number_of_enemies = 6
list_of_enemies = []
for _ in range(number_of_enemies):
    list_of_enemies.append(enemy.Enemy())

# Game Loop
running = True
while running:
    # Adding background image to the screen
    screen.blit(background, (0, 0))

    # Checking for keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.set_player_X_change(-5)
            if event.key == pygame.K_RIGHT:
                player.set_player_X_change(5)
            if event.key == pygame.K_SPACE:
                if bullet.get_bullet_state() == "ready":
                    bulletSound = pygame.mixer.Sound("music/laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bullet.set_bullet_x(player.get_player_x())
                    bullet.set_bullet_state_fire()
                    game_functions.fire_bullet(screen,bullet.get_bullet_img(), bullet.get_bullet_x(),bullet.get_bullet_y())

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.set_player_X_change(0)

    # Player movement
    player.player_move()
    bullet.bullet_move(screen)

    for single_enemy in list_of_enemies:
        game_over = single_enemy.enemy_move(screen)
        # Collision
        collision = game_functions.isCollision(single_enemy.get_enemy_x(), single_enemy.get_enemy_y(), bullet.get_bullet_x(), bullet.get_bullet_y(), bullet.get_bullet_state())
        if collision:
            explosionSound = pygame.mixer.Sound("music/explosion.wav")
            explosionSound.play()
            bullet.set_bullet_y(680)
            bullet.set_bullet_state_ready()
            score_value += 1
            single_enemy.reset_enemy_when_destroyed()
        if game_over:
            game_functions.game_over_text(screen)
            break

    game_functions.draw_player(screen,player)
    game_functions.show_score(screen,score_value)
    pygame.display.update()

# Quiting Pygame
pygame.quit()