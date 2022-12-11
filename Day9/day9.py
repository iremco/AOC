import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def updateMatrix(temp_location, t_location):
    x_diff= temp_location[0]-t_location[0]
    y_diff= temp_location[1]-t_location[1]
    if(abs(x_diff)==2):
        t_location[0]= (temp_location[0]+t_location[0])//2
        if (abs(y_diff)==1):
            t_location[1]= temp_location[1]
    if(abs(y_diff)==2):
        t_location[1]= (temp_location[1]+t_location[1])//2
        if(abs(x_diff)==1):
            t_location[0]= temp_location[0]            
    return t_location, temp_location

def updateLocation(input, knot_locations):
    global visit_matrix9, visit_matrix
    steps= int(input[1])
    direction= input[0]
    for _ in range(steps):
        if(direction=='R'):
            knot_locations[0]= [knot_locations[0][0]+1, knot_locations[0][1]]
        elif (direction=='L'):
            knot_locations[0]= [knot_locations[0][0]-1, knot_locations[0][1]]
        elif(direction=='U'):
            knot_locations[0]= [knot_locations[0][0], knot_locations[0][1]+1]
        elif(direction=='D'):
            knot_locations[0]= [knot_locations[0][0], knot_locations[0][1]-1]
        for i in range(len(knot_locations)-1):
            knot_locations[i+1], knot_locations[i] = updateMatrix(knot_locations[i], knot_locations[i+1])
            if(i==0):
                visit_matrix[knot_locations[i+1][0]][knot_locations[i+1][1]]=1
        visit_matrix9[knot_locations[i+1][0]][knot_locations[i+1][1]]=1
    return knot_locations

def getVisitedLocations():
    global visit_matrix9, visit_matrix
    knot_locations=[[500,500] for  _ in range(10)]
    visit_matrix = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]
    visit_matrix9 = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]
    visit_matrix[500][500]=1
    visit_matrix9[500][500]=1
    with open(file_path) as f:
        for line in f:
            knot_locations= updateLocation(line.replace('\n', '').split(' '),knot_locations)
            visit_matrix[knot_locations[1][0]][knot_locations[1][1]]=1
    visited_spots=0
    for i in range(1000):
        for j in range(1000):
            visited_spots += visit_matrix[i][j]
    visited_spots_9=0
    for i in range(1000):
        for j in range(1000):
            visited_spots_9 += visit_matrix9[i][j]
    return visited_spots, visited_spots_9

def main():
    print("***************************************** \n\n\n DAY9 \n\n\n*****************************************\n\n")
    print('Number of visited Locations:' , getVisitedLocations() )

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)