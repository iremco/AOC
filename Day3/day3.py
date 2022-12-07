import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def getPriority(c):
    if(ord(c)>=97):
        return ord(c)-96
    else:
        return ord(c)-38

def getPriorityValue(first_part,second_part):
    for c1 in first_part:
            for c2 in second_part:
                if c1==c2:
                    return getPriority(c1)

def getPriorityValueSecondPart(list):
    common_list=[]
    for c1 in list[0]:
        for c2 in list[1]:
            if c1==c2:
                common_list.append(c1)
    for c3 in list[2]:
        for c in common_list:
            if c3==c:
                 return getPriority(c)
   
def calculatePriorities():
    total_points = 0
    with open(file_path) as f:
     for line in f:
        first_part, second_part = line[:len(line)//2], line[len(line)//2:]
        total_points+= getPriorityValue(first_part, second_part)
    f.close()
    return total_points

def calculatePrioritiesSecond():
    item_list=[]
    total_points = 0
    with open(file_path) as f:
     for line in f:
        item_list.append(line)
        if len(item_list) == 3:
            total_points+= getPriorityValueSecondPart(item_list)
            item_list=[]
    f.close()
    return total_points


def main():
    print("***************************************** \n\n\n DAY3 \n\n\n*****************************************\n\n")
    print('Total priority points:' , calculatePriorities())
    print('Total priority points second part:' , calculatePrioritiesSecond())

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)