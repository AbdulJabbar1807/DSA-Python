def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum
    
def main():
    mylist2D = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    
    print(diagonal_sum(mylist2D))
    
if __name__ == "__main__":
    main()