def MatrixPrinting(matrix: list[list]):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[i])):
            row += str(matrix[i][j]) + ", "
        print(row)