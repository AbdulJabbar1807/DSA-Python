import array

def pop_array(arr):
    arr.pop(1)
    
def main():
    arr = array.array('i',[10,20,30,40,50])
    pop_array(arr)
    
    print(arr)
    
if __name__ == "__main__":
    main()