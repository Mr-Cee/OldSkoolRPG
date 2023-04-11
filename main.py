import pygame
from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial', 32)
        self.running = True

    def new(self):
        # a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()

    def update(self):
        # Code for updating game

    def draw(self):
        # Code for drawing to screen

    def main(self):
        # Main Game Loop

    def game_over(self):
        # Code for game over conditions

    def intro_screen(self):
        # Code for showing introduction screen


