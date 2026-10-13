import array

def insert_array(arr,index_pos,num):
    if index_pos > len(arr):
        print("Can't insert as array length is short.")
    else:
        arr.insert(index_pos,num)
        
def main():
    arr = array.array('i',[1,3,5,7])
    insert_array(arr,1,2)
    print(arr)
    
if __name__ == "__main__":
    main()