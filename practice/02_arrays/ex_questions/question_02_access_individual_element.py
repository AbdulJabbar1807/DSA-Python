import array 

def access_individual_element(arr):
    for i in range(len(arr)):
        print(arr[i])
        

def main():
    arr = array.array('i',[12,13,15,16])
    access_individual_element(arr)
    
    print(f"Element 1:{arr[0]}\nElement 2:{arr[1]}\nElement 3:{arr[2]}\nElement 4:{arr[3]}")
    
if __name__ == "__main__":
    main()