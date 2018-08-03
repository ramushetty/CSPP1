'''# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
    square root
    '''
    s_s = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    #step = 0.1
    # your code starts here
    i_i = 0.1
    g_g = 0
    while abs(g_g**2 - s_s) >= epsilon:
        g_g = g_g + i_i
    print(g_g)
if __name__ == "__main__":
    main()
