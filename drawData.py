import matplotlib.pyplot as plt
import csv


#Type,Average path length,Average average cost,Average max cost,Average squares checked,Average time,Completion percentage

def drawData():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    
    types = [data[i][0] for i in range(1, len(data))]
    avgPathLength = [float(data[i][1]) for i in range(1, len(data))]
    avgAvgCost = [float(data[i][2]) for i in range(1, len(data))]
    avgMaxCost = [(2 - float(data[i][3])) for i in range(1, len(data))]
    avgSquaresChecked = [float(data[i][4]) for i in range(1, len(data))]
    avgTime = [float(data[i][5]) for i in range(1, len(data))]
    completionPercentage = [float(data[i][6]) for i in range(1, len(data))]

    plt.figure()
    plt.bar(types, avgPathLength, label="Average Path Length")
    plt.legend()
    plt.show()

    plt.figure()
    plt.bar(types, avgAvgCost, label="Average Path Cost")
    plt.legend()
    plt.show()

    plt.figure()
    plt.bar(types, avgMaxCost, label="Average Max cost")
    plt.legend()
    plt.show()

    plt.figure()
    plt.bar(types, avgSquaresChecked, label="Average Grid Squares Checked")
    plt.legend()
    plt.show()

    plt.figure()
    plt.bar(types, avgTime, label="Average Time (s)")
    plt.legend()
    plt.show()

    plt.figure()
    plt.bar(types, completionPercentage, label="Completion Percentage (%)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    drawData()