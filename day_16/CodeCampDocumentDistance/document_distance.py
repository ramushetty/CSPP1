'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    #print("1   :",dict1)
    #print("2   :",dict2)
    import re
    import math

    d1=""
    d2=""
    d4=[]
    d5=[]
    f={}
    d1 = dict1
    d2 = dict2
    ne1= re.sub(r'[^a-zA-Z ]', '', d1).lower().strip().split()
    ne2= re.sub(r'[^a-zA-Z ]', '', d2).lower().strip().split()
    loa = load_stopwords("stopwords.txt")
    #print(ne1)
    #print(loa)
    for j in ne1:
        if j not in loa:
            d4.append(j)
    for i in ne2:
        if i not in loa:
            d5.append(i)
    for word in d4:
        if word  in f:
           f[word][0]+=1
        else:
            f[word]=[1,0]
    for word in d5:
        if word in f:
            f[word][1]+=1
        else:
            f[word]=[0,1]
    print(f)
    sum =0
    for j in f :
        sum = sum+(f[j][0]*f[j][1])
    numerator = sum 
    sa = 0
    for j in f:
        sa=sa+(f[j][0]**2)
    na = 0
    for j in f:
        na = na + (f[j][1]**2)
    denominator = math.sqrt(sa)*math.sqrt(na)
    sim=numerator/denominator
    return sim

           




def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
