import random
import pygame
import game_functions

class Enemy:
    def __init__(self):
        list_of_enemies_type = ["img/enemy1.png","img/enemy2.png","img/enemy3.png"]
        self.enemyImg = pygame.image.load(random.choice(list_of_enemies_type))
        self.enemyX = random.randint(100, 700)
        self.enemyY = random.randint(50, 150)
        self.enemyX_change = 4
        self.enemyY_change = 40

    def enemy_move(self, screen):
        game_functions.enemy_move_draw(screen, self.enemyImg, self.enemyX, self.enemyY)
        self.enemyX += self.enemyX_change
        if self.enemyX <= 0:
            self.enemyX_change = 4
            self.enemyY += self.enemyY_change
        elif self.enemyX > 736:
            self.enemyX_change = -4
            self.enemyY += self.enemyY_change

        if self.enemyY > 680:
            return True
        return False


    def get_enemy_x(self):
        return self.enemyX

    def get_enemy_y(self):
        return self.enemyY

    def reset_enemy_when_destroyed(self):
        list_of_enemies_type = ["img/enemy1.png", "img/enemy2.png", "img/enemy2.png"]
        self.enemyImg = pygame.image.load(random.choice(list_of_enemies_type))
        self.enemyX = random.randint(100, 700)
        self.enemyY = random.randint(50, 150)

