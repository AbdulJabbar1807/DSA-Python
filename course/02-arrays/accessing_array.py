import array

def access_element(array,index): 
    if index >= len(array): # Time and Space Complexities: O(1)
        return "Index does'nt exist in the array." # Time and Space Complexities: O(1)
    return(array[index]) # Time and Space Complexities: O(1)
    
def main():
    arr = array.array("i",[1,2,3,4,5])
    print(access_element(arr,9))
    
main()