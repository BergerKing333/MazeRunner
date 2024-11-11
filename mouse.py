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
        if pathType == "A_star":
            path = self.A_star()
        elif pathType == "breadth_first":
            path = self.breadth_first_search()
        elif pathType == "depth_first":
            path = self.depth_first_search()
        if path == None:
            print("No path found")
            return None
        print(f"Time to calculate path: {round(time.time() - startTime, 5)} seconds")
        return path

    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom.keys():
            current = cameFrom[current]
            total_path.prepend(current)
        return total_path
    
    def costmapAstar(self):
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
            self.grid.setSquareColor(x, y, 0)