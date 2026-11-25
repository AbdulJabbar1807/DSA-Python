def remove_duplicates(arr):
# Brute force approach
    # for i in range(len(arr)):
    #     for j in range(len(arr)-1):
    #         if arr[i] == arr[j]:
    #             arr.pop(arr[j])
    # return arr

# optimized approach
    seen = set()
    unique_list = []
    for item in arr:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
            
def main():
    mylist = [1,3,2,5,3,4,5]
    print(remove_duplicates(mylist))
    
if __name__ == "__main__":
    main()