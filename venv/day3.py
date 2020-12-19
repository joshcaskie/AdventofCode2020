import csv

def part1():
    grid = []
    with open("../data/day3.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            temp = ""
            for char in line:
                temp += char
            grid.append(temp)

    #print(grid)
    data.close()

part1()