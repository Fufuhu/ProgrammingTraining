
def make_zero(matrix):
    zeroed_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]

    print("zeroed_matrix:"+str(zeroed_matrix))

    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("(i,j)=("+str(i)+","+str(j)+")")
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if row[i] or col[j]:
                zeroed_matrix[i][j] = 0
            else:
                zeroed_matrix[i][j] = matrix[i][j]

    return zeroed_matrix

if __name__ == "__main__":
    matrix = [[1, 0], [3, 4]]
    zeroed_matrix = make_zero(matrix)

    print(zeroed_matrix)

    matrix = [[1,2,3], [4,0,6],[7,8,9]]
    print(make_zero(matrix))