import numpy as np
import pygame
from mouse import mouse

class grid:
    def __init__(self, width=20, height=20, resolution=(1000, 1000), borderThickness=2):
        # self.grid = np.zeros((width, height))
        self.start = None
        self.end = None
        self.grid = np.random.choice([0, 1], size=(width, height, 2), p=[0.7, 0.3])
        self.width = width
        self.height = height
        self.resolution = resolution
        self.borderThickness = borderThickness

        assert self.width == self.height, "The grid must be a square"
        assert resolution[0] == resolution[1], "The resolution must be a square"

        self.squareSize = self.resolution[0] // self.width - borderThickness

    def setStart(self, x, y):
        if self.start != None:
            self.grid[self.start[0], self.start[1], 0] = 0
        x, y = self.convertCoordsToGrid(x, y)
        if self.grid[x, y, 0] == 1:
            return

        self.grid[x, y, 0] = 2
        self.start = (x, y)

    def setEnd(self, x, y):
        x, y = self.convertCoordsToGrid(x, y)
        if self.grid[x, y, 0] == 1:
            return
        self.grid[x, y, 0] = 3
        self.end = (x, y)
        if self.start != None:
            self.castValues()

    def castValues(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x, y, 1] = abs(self.end[0] - x) + abs(self.end[1] - y)
        
        

    def convertCoordsToGrid(self, x, y):
        return x // (self.squareSize + self.borderThickness), y // (self.squareSize + self.borderThickness)
    
    def convertCoordToScreen(self, x, y):
        return x * (self.squareSize + self.borderThickness), y * (self.squareSize + self.borderThickness)
    
    def draw(self, screen):
        self.screen = screen
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, self.getSquareColor(i, j), (i * (self.squareSize + self.borderThickness), j * (self.squareSize + self.borderThickness), self.squareSize, self.squareSize))


    def drawAll(self):
        self.screen.fill((0, 0, 0))
        self.draw(self.screen)
        pygame.display.flip()


    def getNeighbors(self, coords):
        x, y = coords
        neighbors = []
        if x > 0 and self.grid[x-1, y, 0] != 1:
            neighbors.append((x-1, y))
        if x < self.width - 1 and self.grid[x+1, y, 0] != 1:
            neighbors.append((x+1, y))
        if y > 0 and self.grid[x, y-1, 0] != 1:
            neighbors.append((x, y-1))
        if y < self.height - 1 and self.grid[x, y+1, 0] != 1:
            neighbors.append((x, y+1))
        return neighbors

    def getSquareColor(self, x, y):
        val = self.grid[x, y, 0]
        if val == 0:
            return (255, 255, 255)
        elif val == 1:
            return (0, 0, 0)
        elif val == 2:
            return (0, 255, 0)
        elif val == 3:
            return (255, 0, 0)
        elif val == 4:
            return (0, 0, 255)
        elif val == 5:
            return (0, 255, 255)
        else:
            return (255, 255, 255)
        
    def setSquareColor(self, x, y, color):
        self.grid[x, y, 0] = color
        
    def getHeuristic(self, coords):
        return self.grid[coords[0], coords[1], 1]

    