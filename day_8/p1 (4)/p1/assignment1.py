'''# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
#and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial(n_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_n == 0:
        return 1
    if n_n == 1:
        return n_n
    return n_n*factorial(n_n-1)
def main():
    '''
    factorial
    '''
    a_a = input()
    print(factorial(int(a_a)))
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(25500)
    main()
