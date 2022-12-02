import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)
def updateTotalPoints(list):
    global second_player_total
    first_player=0
    second_player=0
    if list[0] == 'A':
        first_player=1
    elif list[0] == 'B':
        first_player=2
    elif list[0] == 'C':
        first_player=3
    if list[1] == 'X':
        second_player=1
    elif list[1] == 'Y':
        second_player=2
    elif list[1] == 'Z':
        second_player=3
    if (second_player - first_player) == -2 or (second_player - first_player) == 1:
        second_player+=6
    elif (second_player - first_player) ==0 :
        second_player+=3
    second_player_total+=second_player

def updateTotalPointsSecondRound(list):
    global second_player_total_2
    first_player=0
    second_player=0
    if list[0] == 'A':
        first_player=1
    elif list[0] == 'B':
        first_player=2
    elif list[0] == 'C':
        first_player=3
    if list[1] == 'X':
        second_player=first_player-1
        if second_player ==0:
            second_player=3
    elif list[1] == 'Y':
        second_player=first_player+3
    elif list[1] == 'Z':
        second_player=first_player+7
        if second_player ==10:
            second_player=7
    second_player_total_2+=second_player

def calculatePoints():
    play_list=[]
    global second_player_total, second_player_total_2
    second_player_total=0
    second_player_total_2=0
    with open(file_path) as f:
     for line in f:
        play_list = line.replace('\n', '').split(' ')
        updateTotalPoints(play_list)
        updateTotalPointsSecondRound(play_list)
    f.close()
    return second_player_total, second_player_total_2


def main():
    print("***************************************** \n\n\n DAY2 \n\n\n*****************************************\n\n")
    print('First Round: My total points:' , calculatePoints()[0])
    print('Second Round: My total points:' , calculatePoints()[1])

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)
