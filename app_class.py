import copy

import pygame
import sys
from settings import *
from Player_class import *
pygame.init()
vec = pygame.math.Vector2
global wall
global coins
global e_pos
from enemy_class import *

from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("D:\Pacman\pacman_beginning.wav")
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play(5)

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.intro = 'intro'
        self.cell_width = MAZE_WIDTH//19
        self.cell_height = MAZE_HEIGHT//15
        self.player = player(self, PLAYER_START_POS)
        self.wall = list()
        self.coins = []
        self.enimes = []
        self.e_pos = []
        self.load(self.wall,self.coins)
        self.make_enimes()
        

        self.load(self.wall, self.coins)

    def run(self):
            while self.running:
                if self.intro == 'intro':
                    self.intro_events()
                    self.intro_update()
                    self.intro_draw()
                elif self.intro == 'playing':
                    self.playing_events()
                    self.playing_update()
                    self.playing_draw()
                else:
                    self.running = False
                self.clock.tick(FPS)
            pygame.quit()
            sys.exit()
########### Helper Functions #################

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self, wall, coins):
        
  
        # Initialing RGB Color 
        color = (0, 0, 255)

        self.background = pygame.image.load(r'capture_the_flagd.jpg')

        self.background = pygame.transform.scale(
            self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        with open('walls.txt', 'r', encoding="utf8") as file:
            for yind, line in enumerate(file):
                for xind, char in enumerate(line):
                    if char == '🟥' or char == '🟦':
                        wall.append(vec(xind, yind))
                    if char == '🟡':
                        coins.append(vec(xind, yind))
                    if char == "🤡" or char =="⭕" or char =="😶" or char == "🥰":
                            self.e_pos.append(vec(xind,yind))
                           
    def make_enimes(self):
        for idx,pos in enumerate(self.e_pos):
            self.enimes.append(Enemy(self,vec(pos),idx,self.player.sa))
        

    def draw_grid(self):
        """for x in range(MAZE_WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY,
                             (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
        for x in range(MAZE_HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x *
                             self.cell_height), (WIDTH, x*self.cell_height))"""
        for i in self.wall:
            if(i.x < 20):
                pygame.draw.rect(self.background, (0, 0, 255), (i.x*self.cell_width,
                                 i.y*self.cell_height, self.cell_width, self.cell_height))
            else:
                pygame.draw.rect(self.background, (0, 0, 255), (i.x*self.cell_width,
                                 i.y*self.cell_height, self.cell_width, self.cell_height))

    def draw_coin(self):
        for j in self.coins:
                # pygame.draw.rect(self.background,(255, 255, 255),(j.x*self.cell_width,j.y*self.cell_height,self.cell_width,self.cell_height))
                pygame.draw.circle(self.screen, (227, 210, 154), (int(
                    j.x*self.cell_width)+self.cell_width-18//2, int(j.y*self.cell_height)+self.cell_height+5//2), 5)

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mixer.music.stop()
                self.intro = 'playing'

    def intro_update(self):
        pass

    def intro_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('DISCLAIMER!', self.screen, [
                       213, 15], 40, (128, 11, 11), START_FONT)
        self.draw_text('BLAH! BLAH! BLAH! BLAH! BLAH! BLAH!',
                       self.screen, [152, 100], 20, WHITE, START_FONT)
        self.draw_text('BLAH! BLAH! BLAH! BLAH! BLAH! BLAH!',
                       self.screen, [152, 130], 20, WHITE, START_FONT)
        self.draw_text('BLAH! BLAH! BLAH! BLAH! BLAH! BLAH!',
                       self.screen, [152, 160], 20, WHITE, START_FONT)
        self.draw_text('HOGYA NA BHAI KITNE PADHEGA DISCLAMIER',
                       self.screen, [122, 185], 20, WHITE, START_FONT)
        self.draw_text('SPACE DABA SPACE', self.screen, [
                       220, 300], 20, WHITE, START_FONT)
        pygame.display.update()

#############################################################################
#                                                                           #
#      +++++++++++++++  A* SEARCH ALGORITHM +++++++++++++++++               #
#                                                                           #
#############################################################################
    """def up(self, k):
        
        x = int(k[0])
        y = int(k[1])-1
        if(vec(x, y) not in self.wall and vec(x,y) not in self.array ):
            print("k : ",vec(x,y))
            self.array.append(vec(x,y))
        

    def Right(self, k):
        x = int(k[0])+1
        y = int(k[1])
        if(vec(x, y) not in self.wall and vec(x,y) not in self.array ):
            self.array.append(vec(x,y))

    def Down(self, k):
        x = int(k[0])
        y = int(k[1])+1
        if(vec(x, y) not in self.wall and vec(x,y) not in self.array ):
            self.array.append(vec(x,y))

    def Left(self, k):
        x = int(k[0])-1
        y = int(k[1])
        if(vec(x, y) not in self.wall and vec(x,y) not in self.array ):
            self.array.append(vec(x,y))"""
        

    """def A_star(self, grid_pos):
            curr = self.array.pop()
            print(curr)
            if curr == [7,7]:
                return
            for i in "RDUS":
                if i == 'R':
                    childcell = [int(grid_pos[0]),int(grid_pos[1]+1)]
                elif i == 'D':
                    childcell = [int(grid_pos[0]),int(grid_pos[1]-1)]
                elif i == 'U':
                    childcell = [int(grid_pos[0]+1),int(grid_pos[1])]
                elif i == 'S':
                    childcell = [int(grid_pos[0]-1),int(grid_pos[1])]
                if childcell in self.explored:
                    continue
                self.explored.append(childcell)
                self.array.append(childcell)
                print(self.array,self.explored)
                self.player.move(vec(childcell[0],childcell[1]))
"""

            
        
        
      
##################### Playing Functions #########################

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                elif event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                elif event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                elif event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))
        
        #self.A_star(self.player.grid_pos)
        

    def playing_update(self):
            self.player.update()
            for enemy in self.enimes:
                enemy.update()
        

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER-18,TOP_BOTTOM_BUFFER-10))
        
        self.draw_coin()
        self.draw_grid()
        self.draw_text('HIGH SCORE : {}'.format(self.player.counts), self.screen, [23, -5],
                       START_TEXT_SIZE, WHITE, START_FONT)
        self.draw_text('CURRENT SCORE : {}'.format(self.player.counts), self.screen, [550, -3],
                       START_TEXT_SIZE, (255, 255, 255), START_FONT)
        
        self.player.draw()
        for enemy in self.enimes:
            enemy.draw()
        pygame.display.update()
    


        
            