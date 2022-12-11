import os
import time
script_dir = os.path.dirname(__file__)
input_name = "input.txt"
file_path = os.path.join(script_dir, input_name)

def updateVisibleTreeMatrix(x1, x2, y1, y2, sign):
    global matrix,visible_matrix
    for i in range(x1, x2):
        tallest=-1
        for j in range(y1, y2, sign):
            if tallest < int(matrix[i][j]):
                tallest = int(matrix[i][j])
                visible_matrix[i][j]=1

def updateVisibleTreeMatrixUpside(x1, x2, y1, y2, sign):
    global matrix, visible_matrix
    for i in range(x1, x2):
        tallest=-1
        for j in range(y1, y2, sign):
            if tallest < int(matrix[j][i]):
                tallest = int(matrix[j][i])
                visible_matrix[j][i]=1

def createMatrix():
    global matrix, visible_matrix
    matrix=[]  
    with open(file_path) as f:
        for line in f:
            matrix.append(line.replace('\n', ''))
    f.close()
    rows= int(len(matrix))
    columns = int(len(matrix[0]))
    visible_matrix = [ [ 0 for i in range(rows) ] for j in range(columns) ]
    updateVisibleTreeMatrix(0, rows, 0, columns, 1)
    updateVisibleTreeMatrix(0, rows, columns-1, -1, -1)
    updateVisibleTreeMatrixUpside(0, columns, 0, rows, 1)
    updateVisibleTreeMatrixUpside(0, columns, rows-1, -1, -1)

    total_number=0
    for i in range(rows):
        for j in range(columns):
            total_number+= visible_matrix[i][j]
    return total_number


def updateVisibleTreeMatrix2(x1, x2, y1, y2, sign):
    global matrix,visible_matrix
    for i in range(x1, x2):
        for j in range(y1, y2, sign):
            for k in range(j+sign, y2, sign ):
                if int(matrix[i][k]) >= int(matrix[i][j]):
                    visible_matrix[i][j]=visible_matrix[i][j]*(k-j)
                    break
                if(k == y2-sign):
                    visible_matrix[i][j]=visible_matrix[i][j]*(k-j)

def updateVisibleTreeMatrixUpside2(x1, x2, y1, y2, sign):
    global matrix, visible_matrix
    for i in range(x1, x2):
        for j in range(y1, y2, sign):
            for k in range(j+sign, y2, sign ):
                if int(matrix[k][i]) >= int(matrix[j][i]):
                    visible_matrix[j][i]=visible_matrix[j][i]*(k-j)
                    break
                if(k == y2-sign):
                    visible_matrix[j][i]=visible_matrix[j][i]*(k-j)

def getScenicScore():
    global matrix, visible_matrix
    matrix=[]  
    with open(file_path) as f:
        for line in f:
            matrix.append(line.replace('\n', ''))
    f.close()
    rows= int(len(matrix))
    columns = int(len(matrix[0]))
    visible_matrix = [ [ 1 for i in range(rows) ] for j in range(columns) ]
    updateVisibleTreeMatrix2(0, rows, 0, columns, 1)
    updateVisibleTreeMatrix2(0, rows, columns-1, -1, -1)
    updateVisibleTreeMatrixUpside2(0, columns, 0, rows, 1)
    updateVisibleTreeMatrixUpside2(0, columns, rows-1, -1, -1)
    max_score=0
    for i in range(0,rows):
        for j in range(0, columns):
            if max_score < visible_matrix[i][j]:
                max_score = visible_matrix[i][j]
    return max_score

def main():
    print("***************************************** \n\n\n DAY8 \n\n\n*****************************************\n\n")
    print('Visible trees:' , createMatrix())
    print('Max Scenic Score:' , getScenicScore())

if __name__ == "__main__":
    start= time.time()
    main()
    print('runtime:', time.time()-start)