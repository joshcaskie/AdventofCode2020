import csv

def part1():
    #Store data in a list of lists // Matrix
    grid = []
    with open("data/day3.csv", newline='') as data:
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

def part2():
    #Store data in a list of lists // Matrix
    grid = []
    with open("../data/day3.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            temp = ""
            for char in line:
                temp += char
            grid.append(temp)

    #Iterate through data by various different methods as defined by the question, then multiply the number of trees
    ans = 1
    rightList = [1,3,5,7] #These are all right by ____ down by 1
    for loop in rightList:
        trees = 0
        loc = 0
        for i in range(len(grid)):
            if (i == 0):
                loc += loop
                continue

            if (grid[i][loc % len(grid[0])] == '#'):  #Mod divide because we want to go through the whole "mountain" of data on the toboggan
               trees += 1

            loc += loop

        ans *= trees

    #Now I need right by 1 down by 2
    trees = 0
    loc = 0
    for i in range(0, len(grid), 2):
        if (i == 0):
            loc += 1
            continue

        if (grid[i][loc % len(grid[0])] == '#'):  # Mod divide because we want to go through the whole "mountain" of data on the toboggan
            trees += 1

        loc += 1

    ans *= trees

    print(ans)
    data.close()

part1()
part2()