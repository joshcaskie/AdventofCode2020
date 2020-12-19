import csv

#initial ideas are to check each line manually
# 6-13 h: pghjchdxhnjhjd
# Check for numbers up to the '-' and then check for numbers up to the first ' '. Then next letter 'x' and ': ' and then start checking the string
# Is there a way to streamline this? Or do I have to do it manually?

def part1():

    numCorrect = 0

    with open("../data/day2.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:
            #length = len(line)
            #realLine = str(line)
            #length = len(realLine)       #For some reason - directly computing the length of the line from the CSV reader gives a length of 1
            #The above method is broken as well
            realLine = ""
            for i in line:
                realLine += i
            length = len(realLine)

            index = 0
            firstNum = 0
            secondNum = 0
            ################################
            #Get the first number
            while (line[0][index] != '-'):
                firstNum = firstNum * 10 + int(line[0][index])    #manually scanning the string for numbers and increasing accordingly by base 10
                #print(int(line[index][0]))
                index += 1

            #if (line[0][index] == '-'):
            index += 1

            #Second number
            while (line[0][index] != ' '):
                secondNum = secondNum * 10 + int(line[0][index])    #manually scanning the string for numbers and increasing accordingly by base 10
                index += 1

            #if (line[0][index] == ' '):
            index += 1

            #print(firstNum)
            #print(secondNum)

            #Grab the character to search for
            char = line[0][index]

            #print(char)

            #if(line[0][index] == ':' or line[0][index] == ' '):
            index += 2

            #Start looping through the rest of the list!
            count = 0
            while (index < length):
                #print(line[0][index])
                if (line[0][index] == char):
                    count += 1
                index += 1

            if (count >= firstNum and count <= secondNum):
                numCorrect += 1
        ####################################

    data.close()

    print(numCorrect)

def part2():

    numCorrect = 0

    with open("../data/day2.csv", newline='') as data:
        reader = csv.reader(data)
        for line in reader:

            realLine = ""
            for i in line:
                realLine += i
            length = len(realLine)

            index = 0
            firstNum = 0
            secondNum = 0

            #Get the first number
            while (line[0][index] != '-'):
                firstNum = firstNum * 10 + int(line[0][index])
                #print(int(line[index][0]))
                index += 1

            index += 1

            #Second number
            while (line[0][index] != ' '):
                secondNum = secondNum * 10 + int(line[0][index])
                index += 1

            index += 1

            #Grab the character to search for
            char = line[0][index]

            index += 2

            #Save the rest of the string separately for analysis
            actual = ""
            while (index < length):
                actual += line[0][index]
                index += 1

            r = range(firstNum, secondNum + 1)   #I have no idea why it's not doing index 0 based operations
            found = False
            wrong = True
            for i in r:
                print(i)
                print(actual[i])
                if (actual[i] == char):
                    found = True
                    wrong = False
                elif (found):
                    wrong = True   #capitalized in python

            if (not wrong and found):
                numCorrect += 1



    data.close()

    print(numCorrect)


part1()
part2()