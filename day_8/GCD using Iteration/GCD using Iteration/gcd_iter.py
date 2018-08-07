# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns
#the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a_a, b_b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for i_i in range(1, max(a_a, b_b)+1):

        if a_a%i_i == 0 and b_b%i_i == 0:
            n_n=i_i

    return n_n
def main():
    '''
    gcd ofa numberS
    '''
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()