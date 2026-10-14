import numpy as np

def main():
    twoDArray = np.array([[1,2,3],[11,12,13],[21,22,23],[31,32,33]])
    print(twoDArray)
    
    newTDArray = np.delete(twoDArray,2,axis=0)
    print(newTDArray)
    
if __name__ == "__main__":
    main()