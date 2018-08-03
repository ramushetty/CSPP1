# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    # input is captured in s
    s = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    c_c = 0
    while c_c**3 < s:
        c_c = c_c+1
    if c_c**3 != s:
        print(str(s)+' is not a perfect cube')
    else:
        print(str(s)+' is a perfect cube')

if __name__ == "__main__":
    main()
