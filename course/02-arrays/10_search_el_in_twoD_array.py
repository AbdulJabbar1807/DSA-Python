import numpy as np

def search_el_in_two_D_array(array,target):
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == target:
                    return(f"element {target} found at index {i,j}.")
                
        return(f"element {target} not found.")

def main():
    twoDArray = np.array([[1,2,3],[11,12,13],[21,22,23],[31,32,33]])
    print(twoDArray)
    
    print(search_el_in_two_D_array(twoDArray,22))
    
if __name__ == "__main__":
    main()

