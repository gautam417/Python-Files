# CIS 41B Assignment 1
# Name: Gautam Mehta

from scores import Scores
    
def main() :
    data = Scores()     # create Scores object
    gen=data.getOne()   # create generator object
    print(next(gen))    # fetch first data of object
    data.printByLast()  # print all data sorted by last field
    print(next(gen))    # fetch next data of object
    data.printMaxMin()  # print the max and min of the total scores
    print(next(gen))    # fetch next data of object
    
main()