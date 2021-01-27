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
    uniqueIDs = []

    for i in range(arr.size):
        row = np.array(range(128))
        col = np.array(range(8))

        #idea is to split the lists and save only the HALF that we want to keep based on the scenario

        seat = arr[i]

        #Row Calculation
        row_split = int(128 / 2)
        for r in range(7):
            if seat[r] == 'F': #Take the lower half of 128
                row = row[:row_split]
            else: #Take the upper half of 128
                row = row[row_split:]
            row_split = int(row_split / 2)

        #Column Calculation
        col_split = int(8 / 2)
        for c in [7,8,9]:
            if seat[c] == 'L': #Take the lower half of 8
                col = col[:col_split]
            else: #Take the upper half of 128
                col = col[col_split:]
            col_split = int(col_split / 2)

        uniqueIDs.append(row[0] * 8 + col[0])

    print(uniqueIDs)

    #Get the largest ID in the list
    ans = -1
    for i in uniqueIDs:
        if i > ans:
            ans = i

    print(ans)

#Error debugging / my code to find the ID is correct, but my largest number finder is not
def get3B():
    arr = np.array(getData())
    for i in range(arr.size):
        seat = arr[i]
        if seat[0] == 'B' and seat[1] == 'B' and seat[2] == 'B':
            print(seat)


#get3B()

highestSeatID()