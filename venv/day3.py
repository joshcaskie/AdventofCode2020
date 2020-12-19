import csv

def part1():
    #Store data in a list of lists // Matrix
    grid = []
    with open("../data/day3.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            temp = ""
            for char in line:
                temp += char
            grid.append(temp)

    #Iterate through data going 3 across and 1 down while checking for trees.
    loc = 0
    for i in range(len(grid)):
        if (i == 0):
            continue
        elif (loc < len(grid[0])):
            if (grid[i][loc] == '#'):
               print("tree")
            else:
                print("clear")
        loc += 3

    #print(grid)
    data.close()

part1()