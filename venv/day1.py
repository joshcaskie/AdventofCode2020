#https://adventofcode.com/2020/
#https://www.w3schools.com/python/
#https://docs.python.org/3/library/csv.html

def day1():
    file = open("..\data\day1.csv") #. is the current directory, and .. goes up one directory (talked about in 220 file i/o)
    list: List[Int] = [10]
    for i in file:
        int(print(i))

    file.close()
    print(list)


day1()
