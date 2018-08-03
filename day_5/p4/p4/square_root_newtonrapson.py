'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    '''
    newton rapson
    '''
    s_s = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    # your code starts here
    k_k = s_s/2.0
    while abs (k_k*k_k - s_s) >= epsilon:
        k_k = k_k - (((k_k**2) - s_s ) / (2*k_k))
    print(str(k_k))

if __name__ == "__main__":
    main()
