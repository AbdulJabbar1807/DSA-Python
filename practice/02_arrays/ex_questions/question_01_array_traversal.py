import array 

def array_traversal(arr):
    for i in arr:
        print(i)

def main():
    arr = array.array('i',[1,3,5,6])
    array_traversal(arr)
    
if __name__ == "__main__":
    main()
    