# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdRecur(a, b, i):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if i==min(a,b):
    	return gcd
    if a%i==0 and b%i==0:
    	gcd = i
    return gcd(a,b,i+1)

    


def main():
	i=1
	data = input()
	data = data.split()
	print(gcdRecur(int(data[0]),int(data[1],i))

if __name__ == "__main__":
    main()