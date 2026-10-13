import array

def fromlist_array(arr,list_el):
    arr.fromlist(list_el)

def main():
    arr = array.array('i',[1,2,3,4,5])
    list_el = [11,12,13]
    fromlist_array(arr,list_el)
    
    print(arr)
    
if __name__ == "__main__":
    main()