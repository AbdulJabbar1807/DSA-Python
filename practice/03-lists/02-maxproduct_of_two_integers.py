# def max_product(arr):
#     max_multiple = 1
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             max_multiple = max(max_multiple,arr[i]*arr[j])
#     return max_multiple
    
# Better approach
def max_product(arr):
    max1,max2 = 0,0
    
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
            
    return max1 * max2    
    
def main():
    num = [1,2,3,4,5,6]
    print(max_product(num))
    
if __name__ == "__main__":
    main()
    