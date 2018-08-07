 # Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.

sum = 0
def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n==0:
    	return 0
    else:
    	return (n%10+sumofdigits(n//10))
def main():
	'''
	sum of digits
	'''
    a = input()
    print(sumofdigits(int(a)))  

if __name__ == "__main__":
    main()

