#define the gen_primes function here
def genPrimes():
    number = 2
    while number>0:
    	prime = True
    	for i in range(2, number):
    		if number % i == 0:
    			prime = False
    	if prime:
    		yield number 
    	number += 1

def main():
	data = input()
	l = data.split()
	a = int(l[0])
	b = int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p = primeGenerator.__next__()
	    if(i%b == 0):
	        print (p)
	
if __name__== "__main__":
	main()
