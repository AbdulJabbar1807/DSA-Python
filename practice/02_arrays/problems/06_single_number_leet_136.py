import array

def single_number(nums):
    # nums.sort()
    # for i in range(0,len(nums)-1,2):
    #     if nums[i] == nums[i+1]:
    #         pass
    #     else:
    #         return nums[i]
    # return nums[-1]
    
    res = 0
    for num in nums:
        res ^= num
    return res
    
def main():
    nums = array.array('i',[4,1,2,1,2])
    
    print(single_number(nums))
    
if __name__ == "__main__":
    main()