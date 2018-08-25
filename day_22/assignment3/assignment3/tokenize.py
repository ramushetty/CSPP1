'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def clean_index(index):
    '''
    to remove special characters
    '''
    listt1 = index
    out = re.sub(r'[^a-zA-z]', ' ', listt1).split()
    return out

def tokenize(string):
    '''
    token size
    '''
    listt = string
    dictt = {}
    for index in listt:
        #print(index)
        clean = clean_index(index)
        for j in clean:
            if j in dictt:
                dictt[j] += 1
            else:
                dictt[j] = 1
    return dictt
def main():
    '''
    main
    '''
    intt = int(input())
    doc = []
    for i in range(intt):
        doc.append(input())
    #print(doc)
    print(tokenize(doc))
if __name__ == '__main__':
    main()
