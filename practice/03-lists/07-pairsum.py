def pair_sum(myList, n):
    pairs = []
    for i in range(len(myList)-1):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == n:
                pairs.append(f'{myList[i]}+{myList[j]}')
    return pairs

def main():
    myList = [2,4,3,5,6,-2,4,7,8,9]
    num = 7
    new_list = pair_sum(myList,num)
    print(new_list)
    
if __name__ == "__main__":
    main()