def middle_function(lst):
# brute force approach
    # lst.pop()
    # lst.pop(0)
    
# optimistic approach
    lst = lst[1:-1]
    
    return lst
    
def main():
    mylist = [1,2,3,4,5,6]
    print(middle_function(mylist))
    
if __name__ == "__main__":
    main()