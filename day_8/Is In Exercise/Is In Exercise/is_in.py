# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr, i_i):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if char == aStr[i_i]:
        return True
    if i_i < len(aStr)-1:
        if char != aStr[i_i]:
            return isIn(char, aStr, i_i+1)
    
    return False 
def main():
    data = input()
    i_i = 0
    data = data.split()
    print(isIn((data[0][0]), data[1],i_i))


if __name__== "__main__":
    main()