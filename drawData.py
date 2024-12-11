import matploblib.pyplot as plt
import csv

def drawData():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    types = data[0][1:]
    avgPathLength = [float(i[1]) for i in data[1:]]
    avgAvgCost = [float(i[2]) for i in data[1:]]
    avgMaxCost = [float(i[3]) for i in data[1:]]
    avgSquaresChecked = [float(i[4]) for i in data[1:]]
    avgTime = [float(i[5]) for i in data[1:]]
    completionPercentage = [float(i[6]) for i in data[1:]]
    
    fig, ax = plt.subplots(3, 2)
    ax[0, 0].bar(types, avgPathLength)
    ax[0, 0].set_title("Average path length")
    ax[0, 1].bar(types, avgAvgCost)
    ax[0, 1].set_title("Average average cost")
    ax[1, 0].bar(types, avgMaxCost)
    ax[1, 0].set_title("Average max cost")
    ax[1, 1].bar(types, avgSquaresChecked)
    ax[1, 1].set_title("Average squares checked")
    ax[2, 0].bar(types, avgTime)
    ax[2, 0].set_title("Average time")
    ax[2, 1].bar(types, completionPercentage)
    ax[2, 1].set_title("Completion percentage")
    plt.show()