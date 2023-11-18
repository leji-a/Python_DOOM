from settings import * 
import pygame as pg
import math

class Player: 
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angel = PLAYER_ANGLE
        
    def movement():
        pass
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y