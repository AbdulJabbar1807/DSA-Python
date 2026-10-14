import array

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"found element at {i} index."
        else:
            "Not found."
            
def main():
    arr = array.array('i',[1,2,3,4,5])
    print(linear_search(arr,3))
    
main()