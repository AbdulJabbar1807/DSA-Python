import array

def binary_search(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1

def main():
    nums = array.array('i',[20,30,40,50,60,70,80,90])
    target = 60
    print(binary_search(nums,target))
    
if __name__ == "__main__":
    main()