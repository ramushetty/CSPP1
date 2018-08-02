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
    #print(la)
    ca = 0
    ma = 0
    ja = 0
    for i in range(0, la-1, 1):
        while  string2[ja] == string1[i]:
            if ca == len(string2)-1:
                ja = 0
                ma+= 1
                ca = 0
                continue
            ca+= 1
            ja+= 1
        
    print(ma)

if __name__== "__main__":
    main()
