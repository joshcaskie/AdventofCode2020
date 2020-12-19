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
    trees = 0
    loc = 0
    for i in range(len(grid)):
        #How do I get python to "continue" on the loop // it is continuing - I just wasn't incrementing.
        if (i == 0):
            loc += 3
            continue
        #print(loc % len(grid[0]))
        #print(grid[i][loc % len(grid[0])])
        if (grid[i][loc % len(grid[0])] == '#'):  #Mod divide because we want to go through the whole "mountain" of data on the toboggan
           trees += 1
        #else:
            #print("clear")
        loc += 3

    #print(grid)
    data.close()
    print(trees)

part1()