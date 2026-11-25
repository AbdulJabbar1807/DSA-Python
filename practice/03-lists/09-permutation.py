def is_permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
def main():
    list1 = [1,2,3,4,5]
    list2 = [3,2,1,4,5]
    
    print(is_permutation(list1,list2))
    
if __name__ == "__main__":
    main()