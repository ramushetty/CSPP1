'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    '''
    '''
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    s_s = input()
    k_k = 0
    s_t = ""
    for i in range(0, len(s_s)-1, 1):
        if i == len(s_s):
            break
        if s_s[i] <= s_s[i+1]:
            s_t = s_t+s_s[i]
            if len(s_t)>k_k:
                k_k = len(s_t)
                out = s_t+s_s[i+1]
        else:  
            s_t = ""          
    print(out)

if __name__ == "__main__":
    main()
