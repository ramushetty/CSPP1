#Assume s is a string of lower case characters.

'''Write a program that counts up the number of vowels contained
 in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
 if s = 'azcbobobegghakl', your program should print:'''

#Number of vowels: 5

def main():
    s = input()
    c = 0
    for i in range(0, len(s), 1):
        if s[i] == 'a'or s[i] == 'e'or s[i] == 'i'or s[i] == 'o'or s[i] == 'u':
            c = c+1
    print(c)

if __name__ == "__main__":
	main()
