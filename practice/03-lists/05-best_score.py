def first_second(lst):
    first,second = 0,0
    for score in lst:
        if score > first:
            second = first
            first = score
        elif score > second and score != first:
            second = score
    return first,second

def main():
    mylist = [23,24,34,54,34,65,86,67,87,23,96,54]
    
    print(first_second(mylist))
    
if __name__ == "__main__":
    main()