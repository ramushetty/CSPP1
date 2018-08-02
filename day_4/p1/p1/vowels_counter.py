#Assume s is a string of lower case characters.

'''Write a program that counts up the number of vowels contained
 in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
 if s = 'azcbobobegghakl', your program should print:'''

#Number of vowels: 5

def main():
    '''
    counting vowels
    '''
    s_i = input()
    c_i = 0
    for i in range(0, len(s_i), 1):
        if s_i[i] == 'a'or s_i[i] == 'e'or s_i[i] == 'i'or s_i[i] == 'o'or s_i[i] == 'u':
            c_i = c_i+1
    print(c_i)

if __name__ == "__main__":
    main()
