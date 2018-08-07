# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns
#the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    i=1
    k_k = 0
    while i<=a:
        if a<=b:
           if a%i==0 and b%i==0:
                c_c = a
        i=i+1
    return c_c
def main():
    '''
    gcd ofa number
    '''
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()