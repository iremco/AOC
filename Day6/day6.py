import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def findNumberOfCharactersBeforeFirstPackage(message_size):
    last_four_list=[]
    for i in range(message_size):
        last_four_list.append('')
    with open(file_path) as f:
     for line in f:
        for i in range(len(line)):
            last_four_list[i%message_size]=line[i]
            if(len(set(last_four_list))==message_size and i >=message_size):
                return i+1

def main():
    print("***************************************** \n\n\n DAY6 \n\n\n*****************************************\n\n")
    print('Number of characters before package:' , findNumberOfCharactersBeforeFirstPackage(4))
    print('Number of characters before message:' , findNumberOfCharactersBeforeFirstPackage(14))

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)