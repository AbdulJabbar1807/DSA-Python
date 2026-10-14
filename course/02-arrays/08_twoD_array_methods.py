import numpy as np

# Accessing an element in 2-D Array
def access_2_D_Array(array,rowindex,colindex):
    if rowindex >= len(array) or colindex >= len(array[0]):
        print("Invalid index.")
    else:
        print(array[rowindex][colindex])
    
def main():
    twoDArray = np.array([[1,2,3],[11,12,13],[21,22,23],[31,32,33]])
    print(twoDArray)

    # Insertion
    newtwoDArray_1 = np.insert(twoDArray,1,[[4,5,6,7]],axis=1)
    print(newtwoDArray_1)

    # Append
    newtwoDArray_2 = np.append(twoDArray,[[4,14,24]],axis=0)
    print(newtwoDArray_2)
    #Access
    access_2_D_Array(newtwoDArray_2,5,2)

if __name__ == "__main__":
    main()