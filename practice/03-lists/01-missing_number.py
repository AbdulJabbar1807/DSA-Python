def missing_number(num,n):
    total = n * (n+1)//2
    sum_num = sum(num)
    missing = total - sum_num
    
    return missing

def main():
    num = [1,2,3,4,5,6,7,9]
    n = len(num) + 1
    
    print(missing_number(num,n))
    
if __name__ == "__main__":
    main()
