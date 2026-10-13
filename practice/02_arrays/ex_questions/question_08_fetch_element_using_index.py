import array

def fetch_element_using_index(arr,el):
    return arr.index(el)
        
def main():
    arr = array.array('i',[10,20,30,40,50])
    index = fetch_element_using_index(arr,30)
    print(index)
    
if __name__ == "__main__":
    main()