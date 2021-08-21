import pygame
import math


def show_score(screen, score_value):
    # Setting free font and size for this message
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 7
    textY = 7
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def game_over_text(screen):
    # Game Over font and size.
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 250))


def draw_player(screen, player):
    screen.blit(player.get_player_img(), (player.get_player_x(), player.get_player_y()))


def enemy_move_draw(screen, img, x,y):
    screen.blit(img, (x, y))


def fire_bullet(screen, img, x,y):
    screen.blit(img, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY, bullet_state):
    if bullet_state == "fire":
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
    else:
        return False

