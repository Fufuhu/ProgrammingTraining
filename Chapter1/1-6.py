import math

def rotate(matrix):
    rotater = [[0, 1], [-1, 0]]

    print("**Rotater**")x
    print(str(rotater[0][0]))
    print(str(rotater[0][1]))
    print(str(rotater[1][0]))
    print(str(rotater[1][1]))

    print("row:"+str(len(matrix)))
    print("col:"+str(len(matrix[0])))

    row = len(matrix)
    col = len(matrix[0])


    rotated_matrix = [[0] * col for i in range(row)]
    
    center_col = col / 2
    center_row = col / 2

    i = 0
    while i < row:
        j = 0
        while j < col:
            trans_i = i - (center_col / 2)
            trans_j = j - (center_row / 2)

            # rot_i = -1 * trans_j
            # rot_j = trans_i

            rot_i = trans_j
            rot_j = -1 * trans_i

            ret_i = math.ceil(rot_i + (center_col / 2))
            ret_j = math.ceil(rot_j + (center_row / 2))

            print("(i,j)=("+str(i)+","+str(j)+"), (r_i, r_j) = ("+str(ret_i)+","+str(ret_j)+")")
            rotated_matrix[ret_i][ret_j] = matrix[i][j]
            j += 1
        i += 1
    return rotated_matrix

if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    print(str(matrix[0][0]))
    print(str(matrix[0][1]))
    print(str(matrix[1][0]))
    print(str(matrix[1][1]))

    rotated_matrix = rotate(matrix)
    print(rotated_matrix)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(matrix))