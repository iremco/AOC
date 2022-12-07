import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def findTopStack():
    list_of_lists = []
    firstPartFlag=True
    top_stack=''
    for i in range(9):
        list_of_lists.append([])
    with open(file_path) as f:
     for line in f:
        if line == '\n':
            firstPartFlag=False
            for i in range(9):
                list_of_lists[i].reverse()
            continue
        if(firstPartFlag):
            for i in range(9):
                if(line[i*4+1]!=' '):
                    list_of_lists[i].append(line[i*4+1])
        else:
            move_sequence= [ int(x) for x in line.replace('move ', '').replace(' from', '').replace(' to','').replace('\n', '').split(' ')]
            print(move_sequence)
            for i in range(move_sequence[0]):
                list_of_lists[move_sequence[2]-1].append(list_of_lists[move_sequence[1]-1].pop())
    f.close()
    for i in range(9):
       top_stack+=list_of_lists[i].pop()
    return top_stack

def findTopStackPartTwo():
    list_of_lists = []
    firstPartFlag=True
    top_stack=''
    for i in range(9):
        list_of_lists.append([])
    with open(file_path) as f:
     for line in f:
        if line == '\n':
            firstPartFlag=False
            for i in range(9):
                list_of_lists[i].reverse()
            continue
        if(firstPartFlag):
            for i in range(9):
                if(line[i*4+1]!=' '):
                    list_of_lists[i].append(line[i*4+1])
        else:
            move_sequence= [ int(x) for x in line.replace('move ', '').replace(' from', '').replace(' to','').replace('\n', '').split(' ')]
            list=[]
            for i in range(move_sequence[0]):
                list.append(list_of_lists[move_sequence[1]-1].pop())
            for i in range(move_sequence[0]):
                list_of_lists[move_sequence[2]-1].append(list.pop())
    f.close()
    for i in range(9):
       top_stack+=list_of_lists[i].pop()
    return top_stack


def main():
    print("***************************************** \n\n\n DAY5 \n\n\n*****************************************\n\n")
    print('TopStack:' , findTopStack())
    print('TopStackPartTwo:' , findTopStackPartTwo())

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)