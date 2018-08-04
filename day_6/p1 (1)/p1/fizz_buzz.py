'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    #c_c = 0
    i_i = 1
    for i_i in range(1, num+1):
        if i_i%3 == 0:
            print("Fizz")
        elif i_i%5 == 0:
            print("Buzz")
        else:
             print(i_i)
        if i_i == num+1:
            break
if __name__ == "__main__":
    main()
