import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)
def findMaximumCalories():
    maximum_cal = 0
    current_cal=0
    with open(file_path) as f:
     for line in f:
        caloriesString = line
        if caloriesString == '\n':
            if maximum_cal < current_cal:
                maximum_cal=current_cal
            current_cal=0
        else:
            calories = int(caloriesString) 
            current_cal+=calories

    if maximum_cal < current_cal:
                maximum_cal=current_cal
    f.close()
    return maximum_cal

def updateTopThree():
    global maximum_cal, second_cal, third_cal, current_cal
    if maximum_cal < current_cal:
        third_cal=second_cal
        second_cal = maximum_cal
        maximum_cal=current_cal
    elif second_cal < current_cal:
        third_cal=second_cal
        second_cal = current_cal
    elif third_cal < current_cal:
        third_cal=current_cal
    return maximum_cal, second_cal, third_cal

def findTopThree():
    global maximum_cal, second_cal, third_cal, current_cal
    maximum_cal= 0
    current_cal=0
    second_cal=0
    third_cal=0
    with open(file_path) as f:
     for line in f:
        if line == '\n':
            updateTopThree()
            current_cal=0
        else:
            calories = int(line) 
            current_cal+=calories

    updateTopThree()
    return maximum_cal+second_cal+third_cal

def main():
    print("***************************************** \n\n\n DAY1 \n\n\n*****************************************\n\n")
    print('maximum:' , findMaximumCalories())
    print('top three:', findTopThree())

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)
