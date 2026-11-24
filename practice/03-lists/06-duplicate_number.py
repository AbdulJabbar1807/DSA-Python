def remove_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)-1):
            if arr[i] == arr[j]:
                arr.pop(arr[j])
    return arr

def main():
    mylist = [1,3,2,5,3,4,5]
    print(remove_duplicates(mylist))
    
if __name__ == "__main__":
    main()