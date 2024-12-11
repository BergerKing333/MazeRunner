import pygame
import numpy as np
from grid import grid
from mouse import mouse
import csv

# path length, average cost, max cost, squares checked, time to calculate path
# return len(path), self.getAveragePathCost(path), self.getMaxPathCost(path), len(visited), round(time.time() - startTime, 5)
def bigTest(n):
    types = ["basicAddition", "multiplication", "exponent", "noCostImplementation"]
    seeds_x = np.random.randint(0, 1000, n)
    seeds_y = np.random.randint(0, 1000, n)
    start_coords = np.random.randint(0, 1300, (n, 2))
    end_coords = np.random.randint(0, 1300, (n, 2))
    data = []
    data.append(["Type", "Average path length", "Average average cost", "Average max cost", "Average squares checked", "Average time", "Completion percentage"])
    for type in types:
        avgPathLength = 0
        avgAvgCost = 0
        avgMaxCost = 0
        avgSquaresChecked = 0
        avgTime = 0
        completed = 0
        for i in range(n):
            map = grid(1300, 1300, (1300, 1300), seed_x=seeds_x[i], seed_y=seeds_y[i])
            map.setStart(start_coords[i][0], start_coords[i][1])
            map.setEnd(end_coords[i][0], end_coords[i][1])
            runner = mouse(map)
            pathLength, avgCost, maxCost, squaresChecked, time = runner.start(pathType=type)
            if pathLength != None:
                avgPathLength += pathLength
                avgAvgCost += avgCost
                avgMaxCost += maxCost
                avgSquaresChecked += squaresChecked
                avgTime += time
                completed += 1
        avgPathLength /= n
        avgAvgCost /= n
        avgMaxCost /= n
        avgSquaresChecked /= n
        avgTime /= n
        completionPercentage = completed / n * 100
        print("===============================================================")
        print(f"Type: {type}")
        print(f"Average path length: {avgPathLength}")
        print(f"Average average cost: {avgAvgCost}")
        print(f"Average max cost: {avgMaxCost}")
        print(f"Average squares checked: {avgSquaresChecked}")
        print(f"Average time: {avgTime}")
        print(f"Completion percentage: {completionPercentage}")
        print("===============================================================\n")
        data.append([type, avgPathLength, avgAvgCost, avgMaxCost, avgSquaresChecked, avgTime, completionPercentage])

    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
            
            
if __name__ == "__main__":
    bigTest(100)