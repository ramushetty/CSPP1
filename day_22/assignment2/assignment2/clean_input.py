'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re 
def clean_string(string):
    inputt = string
    #print(inputt)
    out = re.sub('[^a-z]', '', inputt)
    return out

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
