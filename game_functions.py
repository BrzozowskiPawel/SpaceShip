import pygame
import math


def draw_player(screen, player):
    screen.blit(player.get_player_img(), (player.get_player_x(), player.get_player_y()))



