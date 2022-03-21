matrix = [ [1,2,3],[4,5,6],[7,8,9]  ]

for i in range(len(matrix)):
    row = ""
    for j in range(len(matrix[i])):
        row = row + str(matrix[i][j]) + " "
    print(row)