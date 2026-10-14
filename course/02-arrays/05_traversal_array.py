import array

def traversal_arr(array):
    for i in array: # Time complexity: O(n)
        print(i) # Space complexity: O(1)

def main():
    arr = array.array("i",[1,2,3,4,5])
    traversal_arr(arr) 

main()