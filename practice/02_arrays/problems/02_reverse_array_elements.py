import array

# Approach A - TC:O(n),SC:O(n)
# def reverse_array_elements(arr):
#     i = 0
#     arr_1 = array.array('i',arr)
#     while i < len(arr):
#         arr_1[i] = arr[len(arr)-1-i]
#         i += 1
#     return arr_1

# Approach B:TC:O(n),SC:O(1)
def reverse_array_elements(arr):
    i = 0
    while i < len(arr)//2:
        # temp_st = arr[i]
        # temp_e = arr[len(arr)-1-i]
        # arr[i] = temp_e
        # arr[len(arr)-1-i] = temp_st
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
        i += 1
    return arr

def main():
    arr = array.array('i',[10,20,30,40,50,60,70,80,90,100,110])
    reversed_arr = reverse_array_elements(arr)
    print(f"Reversed Array: {reversed_arr}")
    
if __name__ == "__main__":
    main()