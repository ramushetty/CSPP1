'''
Given a  number int_input, find the product of all the digits
#example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = (int(input()))
    pro = 1
    if int_input == 0:
        print(0)
    elif int_input <= 0:
        k = abs(int_input)
        while k != 0:
            l_l = k%10
            pro = pro*l_l
            k = k // 10
        print(-pro)
    else:
        while int_input != 0:
            l_l = int_input%10
            pro = pro*l_l
            int_input = int_input // 10
        print(pro)
if __name__ == "__main__":
    main()
