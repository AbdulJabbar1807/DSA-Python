import array

def reverse_array_reverse_method(arr):
    arr.reverse()
    return arr
    
def main():
    arr = array.array('i',[10,20,30,40,50])
    reverse_array_reverse_method(arr)
    print(arr)
    
if __name__ == "__main__":
    main()

