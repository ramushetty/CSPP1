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
    if base == 0 and exp == 0:
    	return 0
    else:
    	i = 1
    	base_1 = 1
    	for i in range(i,exp+1):
    		base_1 = base_1*base
    return base_1
def main():
	'''
	power
	'''
	data = input()
	data = data.split()
	print(iterPower(float(data[0]),int(data[1])))

if __name__ == "__main__":
    main()