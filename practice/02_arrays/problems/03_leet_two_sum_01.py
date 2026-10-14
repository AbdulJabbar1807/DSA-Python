import array

def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        j = i+1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return i,j
            j+=1

arr = [2,5,5,11]
target = 10

print(twoSum(arr,target))