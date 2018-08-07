'''# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
#and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial(_n_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if _n_n == 0:
        return 1
    if _n_n == 1:
        return 1
    return _n_n*factorial(_n_n-1)
def main():
    '''s
    factorial
    '''
    a_a = input()
    print(factorial(int(a_a)))
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(255000000)
    main()
