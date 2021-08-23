import pygame
import game_functions


class Bullet:
    def __init__(self):
        self.bulletImg = pygame.image.load('img/bullet.png')
        self.bulletX = 0
        self.bulletY = 680
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = "ready"

    def get_bullet_state(self):
        return self.bullet_state

    def get_bullet_x(self):
        return self.bulletX

    def get_bullet_y(self):
        return self.bulletY

    def get_bullet_img(self):
        return self.bulletImg

    def set_bullet_x(self, val):
        self.bulletX = val

    def set_bullet_y(self,val):
        self.bulletY = val

    def set_bullet_state_fire(self):
        self.bullet_state = "fire"

    def set_bullet_state_ready(self):
        self.bullet_state = "ready"

    def bullet_move(self, screen):
        if self.bulletY <= 0:
            self.bulletY = 680
            self.bullet_state = "ready"

        if self.bullet_state == "fire":
            game_functions.fire_bullet(screen,self.bulletImg,self.bulletX,self.bulletY)
            self.bulletY -= self.bulletY_change