import pygame as pg
from utils import *


class Tank():
    def __init__(self):
        self.hp = 3
        self.ammo = 50
        self.pos_x = W//2
        self.pos_y = H//2
        self.ammo_v = 1
        self.pos_ammo = self.pos_y


    def draw(self,screen):
        pg.draw.rect(screen,NEGRO, (self.pos_x, self.pos_y, 50,50))

    def move(self):
        teclas = pg.key.get_pressed()  
        
        
        if teclas[pg.K_UP] and self.pos_y >= 0:  
            self.pos_y -= 1
        if teclas[pg.K_DOWN] and self.pos_y <= H - h_tank: 
            self.pos_y += 1
        if teclas[pg.K_LEFT] and self.pos_x >= 0:   
            self.pos_x -= 1
        if teclas[pg.K_RIGHT] and self.pos_x <= W - w_tank: 
            self.pos_x += 1
        
    def shoot(self,screen):
        
        teclas = pg.key.get_pressed()
        if teclas[pg.K_SPACE]:
            self.pos_ammo += self.ammo_v
            pg.draw.rect(screen,NEGRO, (self.pos_x, self.pos_ammo, 10,10))
            self.pos_ammo = self.pos_y


    
        