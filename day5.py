import csv
import numpy as np

def getData():
    list = []

    with open("data/day5.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            list.append(line[0])
    data.close()
    return list
    #returns a list of strings of all of the seats

def highestSeatID():
    arr = np.array(getData())

    for i in range(len(list)):
        rows = [x for x in range(128)]     #not sure why list(range(128)) doesn't work
        cols = [x for x in range(8)]

        #idea is to start splitting the lists... Better to use a numpy array which I can split?



highestSeatID()