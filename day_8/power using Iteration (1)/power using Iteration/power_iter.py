# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
    	return 1
    if base == 0:
    	return 0
    i=1
    while i<=exp:
    	base = base *base
    	return base

    


def main():

    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__ == "__main__":
	main()