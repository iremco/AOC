import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def isFullIntersection(first,second):
    if(first[0] <= second [0] and first[1] >= second [1] ) or (first[0] >= second [0] and first[1] <= second [1] ) :
        return True
    else:
        return False

def isIntersection(first,second):
    if(first[0] <= second [0] and first[1] >= second [0]) or (first[0] <= second [1] and first[1] >= second [1] ) :
        return True
    else:
        return False

def findIntersections():
    full_intersection = 0
    intersection=0
    with open(file_path) as f:
     for line in f:
        first_part, second_part = line.split(',')
        first = [int(x) for x in first_part.split('-')]
        second =[int(x) for x in second_part.split('-')]
        if(isFullIntersection(first,second)):
            full_intersection+=1
        elif(isIntersection(first,second)):
            intersection+=1
    f.close()
    return full_intersection, intersection+full_intersection

def main():
    print("***************************************** \n\n\n DAY4 \n\n\n*****************************************\n\n")
    print('Number of fully contains:' , findIntersections()[0])
    print('Number of intersections:' , findIntersections()[1])

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)