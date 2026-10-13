import array

def remove_array(arr,element):
    if element in arr:
        arr.remove(element)
        print(f"{element} removed successfully.")
    else:
        print(f"{element} not in the array.")

def main():
    arr = array.array('i',[10,20,30,40,50])
    remove_array(arr,20)
    print(arr)
    
if __name__ == "__main__":
    main()