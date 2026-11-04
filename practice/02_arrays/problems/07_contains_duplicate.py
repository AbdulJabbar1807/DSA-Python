import array

def contains_duplicate(nums):
    ...
    
def sort(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums
            
    
def main():
    nums = array.array('i',[1,2,3,1])
    print(sort(nums))
    
if __name__ == "__main__":
    main()
    