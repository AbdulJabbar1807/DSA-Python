import array 

def array_append(arr):
    arr.append(34)

def main():
    arr = array.array('i',[1,3,5,6])
    
    print("1.",end="")
    arr.append(23)
    print(arr)
    
    print("2.",end="")
    array_append(arr)
    print(arr)

if __name__ == "__main__":
    main()