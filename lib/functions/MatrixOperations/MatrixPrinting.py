def MatrixPrinting(matrix: list[list]):
    for i in range(len(matrix)):
        row = "["
        for j in range(len(matrix[i])):
            row += str(matrix[i][j]) + (", " if (j < len(matrix[i]) - 1) else "")
        row += "]"
        print(row)