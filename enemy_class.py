from numpy import number
import pygame , random
vec = pygame.math.Vector2
from settings import *
from Player_class import *

class Enemy:
    def __init__(self,app,pos,num,SA):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.num = num
        self.direction = vec(1,0)
        self.personality = self.set_personality()
        self.sa = SA
        self.speed = 2
        print(self.sa)
    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER,(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER)
    def update(self):
        self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            self.move()
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER+self.app.cell_width//2)//self.app.cell_width
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER+self.app.cell_height//2)//self.app.cell_height
            
            
    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1,0) or self.direction == vec(-1,0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER) % self.app.cell_height == 0:
            if self.direction == vec(0,1) or self.direction == vec(0,-1):
                return True
        return False
    def move(self):
        if self.personality == "random":
            self.direction = self.get_random_direction()
        if self.personality == "slow":
            self.direction = self.get_path_direction()
        if self.personality == "speedy":
            self.direction = self.get_path_direction()
        if self.personality == "scared":
            self.direction = self.get_path_direction()
    
    def draw(self):
        if(self.num == 0):
            pygame.draw.circle(self.app.screen,(255, 0, 0),(int(self.pix_pos.x),int(self.pix_pos.y)),7)
        elif(self.num == 1):
            pygame.draw.circle(self.app.screen,(255, 184, 255),(int(self.pix_pos.x),int(self.pix_pos.y)),7)
        elif(self.num == 2):
            pygame.draw.circle(self.app.screen,(0, 255, 255),(int(self.pix_pos.x),int(self.pix_pos.y)),7)
        elif(self.num == 3):
            pygame.draw.circle(self.app.screen,(255, 184, 82),(int(self.pix_pos.x),int(self.pix_pos.y)),7)
    def set_personality(self):
        if(self.num == 0):
            return "speedy"
        elif(self.num == 1):
            return "slow"
        elif(self.num == 2):
            return "random"
        else:
            return "scared"
    def get_random_direction(self):
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                x_dir, y_dir = 1, 0
            elif number == -1:
                x_dir, y_dir = 0, 1
            elif number == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
         
            next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)
            if next_pos not in self.app.wall:
                break
        return vec(x_dir, y_dir)
    
    def get_path_direction(self):
        next_cell = self.find_next_cell_in_path()
        xdir = next_cell[0] - self.grid_pos[0]
        ydir = next_cell[1] - self.grid_pos[1]
        return vec(xdir, ydir)
    def find_next_cell_in_path(self):
        
        path = self.BFS([int(self.grid_pos.x), int(self.grid_pos.y)], [int(self.app.player.grid_pos.x),int(self.app.player.grid_pos.y)])
        print(path[1])
        print(path[1])
        
        return path[1]
    def BFS(self, start, target):
        grid = [[0 for x in range(19)] for x in range(15)]
        for cell in self.app.wall:
            if cell.x < 19 and cell.y < 15:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest

