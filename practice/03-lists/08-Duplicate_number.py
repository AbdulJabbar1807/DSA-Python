def contains_duplicate(nums):
    seen = set()
    for item in nums:
        if item not in seen:
            seen.add(item)
        else:
            return True
    return False

def main():
    nums = [1,2,3,4,1]
    print(contains_duplicate(nums))
    
if __name__ == "__main__":
    main()
