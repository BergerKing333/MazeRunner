from grid import *
import numpy as np
from heapq import heappush, heappop
import time

class mouse:
    def __init__(self, grid, animate=False):
        self.grid = grid
        self.animate = animate

    def start(self, pathType="A_star"):
        startTime = time.time()
        
        if pathType == "basicAddition":
            path, visited = self.basicAddition()
        elif pathType == "noCostImplementation":
            path, visited = self.noCostImplementation()
        elif pathType == "multiplication":
            path, visited = self.multiplication()
        elif pathType == "exponent":
            path, visited = self.exponent()
        if path == None:
            print("No path found")
            return None, None, None, None, None
        # print(f"Time to calculate path: {round(time.time() - startTime, 5)} seconds")
        # path length, average cost, max cost, squares checked, time to calculate path
        return len(path), self.getAveragePathCost(path), self.getMaxPathCost(path), len(visited), round(time.time() - startTime, 5)

    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom.keys():
            current = cameFrom[current]
            total_path.prepend(current)
        return total_path
    
    def getAveragePathCost(self, path):
        total = 0
        for node in path:
            total += self.grid.getCost(node)
        return 2 - (total / len(path))
    
    def getMaxPathCost(self, path):
        maxCost = 10
        for node in path:
            # accommodating for everything being 2 - cost
            maxCost = min(maxCost, self.grid.getCost(node))
        return maxCost
    
    def noCostImplementation(self):
        start = self.grid.start
        openSet = []
        heappush(openSet, (0, start))

        cameFrom = {}
        cameFrom[start] = None
        g_score = {start: 0}
        visited = []
        while openSet:
            current_cost, current_node = heappop(openSet)
            visited.append(current_node)
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                # print(f"Squares checked: {len(visited)}")
                # print(f"Path length: {len(path)}")
                return path[::-1], visited
            for neighbor, score in self.grid.getNeighbors(current_node):
                tentative_g_score = g_score[current_node] + score
                if neighbor not in g_score:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.grid.getHeuristic(neighbor)
                    heappush(openSet, (f_score, neighbor))
                    cameFrom[neighbor] = current_node
        return None, visited
    
    def basicAddition(self):
        start = self.grid.start
        openSet = []
        heappush(openSet, (0, start))

        cameFrom = {}
        cameFrom[start] = None
        g_score = {start: 0}
        visited = []
        while openSet:
            current_cost, current_node = heappop(openSet)
            visited.append(current_node)
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                # print(f"Squares checked: {len(visited)}")
                # print(f"Path length: {len(path)}")
                return path[::-1], visited
        
            for neighbor, score in self.grid.getNeighbors(current_node):
                tentative_g_score = g_score[current_node] + score
                if neighbor not in g_score:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.grid.getHeuristic(neighbor) + (1 / (self.grid.getCost(neighbor) + 1))
                    heappush(openSet, (f_score, neighbor))
                    cameFrom[neighbor] = current_node
        return None, visited
    
    def multiplication(self):
        start = self.grid.start
        openSet = []
        heappush(openSet, (0, start))

        cameFrom = {}
        cameFrom[start] = None
        g_score = {start: 0}
        visited = []
        while openSet:
            current_cost, current_node = heappop(openSet)      
            visited.append(current_node)
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                return path[::-1], visited
        
            for neighbor, score in self.grid.getNeighbors(current_node):
                tentative_g_score = g_score[current_node] + score
                if neighbor not in g_score:
                    g_score[neighbor] = tentative_g_score
                    f_score = (tentative_g_score + self.grid.getHeuristic(neighbor)) * ((2 - self.grid.getCost(neighbor)))
                    heappush(openSet, (f_score, neighbor))
                    cameFrom[neighbor] = current_node
        return None, visited
    
    def exponent(self):
        start = self.grid.start
        openSet = []
        heappush(openSet, (0, start))

        cameFrom = {}
        cameFrom[start] = None
        g_score = {start: 0}
        visited = []
        while openSet:
            current_cost, current_node = heappop(openSet)
            visited.append(current_node)
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                return path[::-1], visited
        
            for neighbor, score in self.grid.getNeighbors(current_node):
                tentative_g_score = g_score[current_node] + score
                if neighbor not in g_score:
                    g_score[neighbor] = tentative_g_score
                    f_score = (tentative_g_score + self.grid.getHeuristic(neighbor)) ** (2 - self.grid.getCost(neighbor))
                    heappush(openSet, (f_score, neighbor))
                    cameFrom[neighbor] = current_node
        return None, visited

    def A_star(self):
        start = self.grid.start
        openSet = []
        heappush(openSet, (0, start))

        cameFrom = {}
        cameFrom[start] = None
        g_score = {start: 0}
        visited = []
        while openSet:
            current_cost, current_node = heappop(openSet)
            if self.animate:
                visited.append(current_node)
                self.drawVisited(visited)
                # self.grid.drawAll()
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                print(f"Squares checked: {len(visited)}")
                return path[::-1], visited
        
            for neighbor in self.grid.getNeighbors(current_node):
                tentative_g_score = g_score[current_node] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.grid.getHeuristic(neighbor)
                    heappush(openSet, (f_score, neighbor))
                    cameFrom[neighbor] = current_node
        return None, visited


    def breadth_first_search(self):
        start = self.grid.start

        openSet = [start]
        cameFrom = {}
        cameFrom[start] = None
        visited = []
        while openSet:
            current_node = openSet.pop(0)
            if self.animate:
                visited.append(current_node)
                self.drawVisited(visited)
                self.grid.drawAll()
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                return path[::-1], visited
            
            for neighbor in self.grid.getNeighbors(current_node):
                if neighbor not in cameFrom:
                    cameFrom[neighbor] = current_node
                    openSet.append(neighbor)
        return None, visited
    
    def depth_first_search(self):
        start = self.grid.start

        openSet = [start]
        cameFrom = {}
        cameFrom[start] = None
        visited = []
        while openSet:
            current_node = openSet.pop(-1)
            if self.animate:
                visited.append(current_node)
                self.drawVisited(visited)
                self.grid.drawAll()
            if current_node == self.grid.end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = cameFrom[current_node]
                return path[::-1], visited
            
            for neighbor in self.grid.getNeighbors(current_node):
                if neighbor not in cameFrom:
                    cameFrom[neighbor] = current_node
                    openSet.append(neighbor)
        return None, visited


    def drawPath(self, path):
        if path == None:
            return
        for node in path[1:-1]:
            x, y = node
            self.grid.setSquareColor(x, y, 4)
    
    def drawVisited(self, visited):
        if visited == None:
            return
        for node in visited[1:-1]:
            x, y = node
            self.grid.setSquareColor(x, y, 5)
    
    
    def clearPath(self, path):
        if path == None:
            return
        for node in path:
            x, y = node
            self.grid.setSquareColor(x, y, self.grid.getCost(node))