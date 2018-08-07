''' # Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and
returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''
def sumofdigits(n_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n
    '''
    # Your code here
    if n_n == 0:
        return 0
    return n_n%10+sumofdigits(n_n//10)
def main():
    '''
    sum of digits
    '''
    a_a = input()
    print(sumofdigits(int(a_a)))
if __name__ == "__main__":
    main()
