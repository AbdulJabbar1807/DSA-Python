import array

# First approach
# def remove_array(arr,el):
#     for i in range(len(arr)):
#         if arr[i] == el:
#             index_pos_el = i
#     for i in range(len(arr)-1):
#         index_pos_el = arr[i+1]

# Second approach
def remove_array(arr,el):
    if el in arr:
        for i in range(len(arr)):
            if arr[i] == el:
                index_pos_el = i
                break

        i = index_pos_el
        while i < len(arr)-1:
            arr[i] = arr[i+1]
            i += 1
        arr.pop(len(arr)-1)
    else:
        print(f"{el} not in the array.")
        
            
def main():
    arr = array.array('i',[10,20,30,10,40,50])
    el = int(input("Enter element to remove: "))
    remove_array(arr,el)
    print(arr)

if __name__ == "__main__":
    main()