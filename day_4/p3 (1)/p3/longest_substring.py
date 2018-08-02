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
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    s=input()
    k=0
    st=""
    for i in range(0,len(s)-1,1):
        if i==len(s):
            break
        if s[i] <= s[i+1]:
            st=st+s[i]
            if len(st)>k:
                k=len(st)
                out=st+s[i+1]
        else:  
            st=""          
    print(out)

if __name__== "__main__":
    main()
