import csv

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
    list = getData()




highestSeatID()