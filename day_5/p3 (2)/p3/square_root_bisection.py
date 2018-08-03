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
    bisection
    '''
    s_s = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    #step = 0.1
    # your code starts her
    g_g = 0
    l_l = 0
    h_h = s_s
    a_a = (h_h+l_l)/2
    while abs(a_a**2-s_s) >= epsilon:
        #print(str(a_a))
        g_g += 1
        if a_a**2 < s_s:
            l_l = a_a
        else:
            h_h = a_a
        a_a = (h_h+l_l)/2.0
    print(str(a_a))

if __name__ == "__main__":
    main()
