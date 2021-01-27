#https://adventofcode.com/2020/
#https://www.w3schools.com/python/
#https://docs.python.org/3/library/csv.html

import csv

def getData():
    list = []

    with open("data/day1.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            list.append(int(line[0]))
        #print(list)
    data.close()
    return list

def part1():
    list = getData()
    #Find two numbers that add to 2020, then print their multiplication
    #O(n^2) runtime on the data set
    length = len(list)
    for i in range(length):
        for j in range(length):
            if i != j and (list[i] + list[j]) == 2020:
                print("Part 1: " + str(list[i] * list[j]))
                return

def part2():
    list = getData()
    #Find three numbers that add to 2020, then print their multiplication
    #O(n^3)
    length = len(list)
    indices = range(length)
    for i in indices:
        for j in indices:
            for k in indices:
                if i != j and i != k and j != k and (list[i] + list[j] + list[k]) == 2020:
                    print("Part 2: " + str(list[i] * list[j] * list[k]))
                    return

part1()
part2()

#Notes:
#Current directory is .   - A directory up is ..
#Review of CSV files in Python
#Look into "typed python" so as to say if types are working properly/warm me about issues? Kind of like Scala?

#Two methods of looping over a list
#1. for loop in list:
#2. length = len(list)
#   for index in range(length):      --> will give indices from 0 to length minus 1

#Not sure if return is the proper way to end the function early?