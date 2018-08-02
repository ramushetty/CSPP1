'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    string1 = input()
    string2 = str("bob")
    la = len(string1)
    print(la)
    c = 0
    m = 0
    j = 0
    for i in range(0, la-1, 1):
        while  string2[j] == string1[i]:
            if c == len(string2)-1:
                j = 0
                m+= 1
                c = 0
                continue
            c+= 1
            j+= 1
        
    print(m)

if __name__== "__main__":
    main()
