import array

def plusone(arr):
    if len(arr) > 1:
        i = 1
        while i < len(arr):
            if arr[(len(arr))-i] == 9:
                arr[len(arr)-i] = 0
                arr[len(arr)-i-1] = arr[len(arr)-i-1] + 1
                break
            else:
                arr[len(arr)-1] = arr[len(arr)-1] + 1
                break
    else:
        if arr[0] < 9:
            arr[0] = arr[0] + 1
        else: 
            arr[0] = 1
            arr.insert(1,0)
            
    return arr

def main():
    arr = array.array('i',[9,9,9])
    new_arr = plusone(arr)
    print(new_arr)
    
if __name__ == "__main__":
    main()
    
    