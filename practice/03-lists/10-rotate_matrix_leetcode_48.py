def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix
    
def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate_matrix(matrix))
    
if __name__ == "__main__":
    main()

