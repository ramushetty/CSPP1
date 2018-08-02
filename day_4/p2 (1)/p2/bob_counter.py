'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''
    to count number of times bob comes in a string
    '''
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    string1 = input()
    string2 = str("bob")
    lal = len(string1)
    #print(la)
    c_a = 0
    m_a = 0
    j_a = 0
    for i in range(0, lal-1, 1):
        while  string2[j_a] == string1[i]:
            if c_a == len(string2)-1:
                j_a = 0
                m_a+= 1
                c_a = 0
                continue
            c_a+= 1
            j_a+= 1
        
    print(m_a)

if __name__ == "__main__":
    main()
