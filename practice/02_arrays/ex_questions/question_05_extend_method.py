import array

def extend_array(arr,arr_1):
    arr.extend(arr_1)

def main():
    arr = array.array('i',[1,2,3,4,5])
    arr_1 = array.array('i',[20,21,22])
    extend_array(arr,arr_1)
    
    print(arr)
    
if __name__ == "__main__":
    main()