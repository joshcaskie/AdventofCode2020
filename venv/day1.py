#https://adventofcode.com/2020/
#https://www.w3schools.com/python/
#https://docs.python.org/3/library/csv.html

import csv

def day1():
    with open("../data/day1.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            print(line)


day1()
