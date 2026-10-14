import numpy as np

def traversal_twoD_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
def main():
    twoDArray = np.array([[1,2,3],[11,12,13],[21,22,23],[31,32,33]])
    print(twoDArray)
    
    traversal_twoD_array(twoDArray)
            
if __name__ == "__main__":
    main()