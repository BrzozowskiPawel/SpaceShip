import pygame


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load('img/spaceship.png')
        self.playerX = 370
        self.playerY = 680
        self.playerX_change = 0

    def get_player_img(self):
        return self.playerImg

    def get_player_x(self):
        return self.playerX

    def get_player_y(self):
        return self.playerY

    def set_player_X_change(self, val):
        self.playerX_change = val

    def player_move(self):
        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736