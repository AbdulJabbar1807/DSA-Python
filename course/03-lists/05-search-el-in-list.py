nums = [1,2,3,4,5,6,7,8,9]

# 'in' operator
num = 2
if num in nums:
    print(f"{num} is in the list.")
else:
    print(f"{num} is not in the list.")
    
# Linear search
def linear_search(nums,target):
    for i,num in enumerate(nums):
        if num == target:
            return i
    return -1

print(linear_search(nums,30))