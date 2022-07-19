from settings import *
from pygame.math import Vector2 as vec
from enemy_class import *
import pygame

from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
crash_sound = pygame.mixer.Sound("D:\Pacman\pacman.wav")

  
# Setting the volume
mixer.music.set_volume(0.2)
  
# Start playing the song

class player:
    def __init__(self,app,pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        
        self.direction = vec(0,1)
        self.stored_direction = None
        self.abel_t_move = True
        self.counts = 0
        self.speed = 2
        self.sa = 0
    def draw(self):
        pygame.draw.circle(self.app.screen,PLAYER_COLOUR1,(int(self.pix_pos.x),int(self.pix_pos.y)),7)
        #pygame.draw.circle(self.app.screen,PLAYER_COLOUR2,(int(self.pix_pos.x),int(self.pix_pos.y+17)),self.app.cell_width//2)
        
    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER,(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER)
        
    def update(self):
        if self.abel_t_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move():
                if self.stored_direction != None:
                    self.direction = self.stored_direction
                self.abel_t_move = self.can_move()
        self.coin()
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height
        
                
            
    def move(self,direction):
        self.stored_direction = direction


    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER) % self.app.cell_height == 0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                return True


    def can_move(self):
        
        for i in self.app.wall:
            if(vec(self.grid_pos+self.direction) == i):
                return False
        return True

        
    def coin(self):
        for i in self.app.coins:
            if(vec(self.grid_pos+self.direction) == i):
                
                self.sa = vec(self.grid_pos+self.direction)
                print(self.sa)
                self.app.coins.remove(vec(self.grid_pos+self.direction))
                pygame.mixer.Sound.play(crash_sound)
                self.counts = self.counts + 1
                
        

       
    