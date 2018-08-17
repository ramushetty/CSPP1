'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import re
    import math

    d_1 = ""
    d_2 = ""
    d_4 = []
    d_5 = []
    f_f = {}
    d_1 = dict1
    d_2 = dict2
    ne_1 = re.sub(r'[^a-zA-Z ]', '', d_1).lower().strip().split()
    ne_2 = re.sub(r'[^a-zA-Z ]', '', d_2).lower().strip().split()
    lo_a = load_stopwords("stopwords.txt")
    #print(ne1)
    #print(loa)
    for j in ne_1:
        if j not in lo_a:
            d_4.append(j)
    for i in ne_2:
        if i not in lo_a:
            d_5.append(i)
    for word in d_4:
        if word  in f_f:
            f_f[word][0] += 1
        else:
            f_f[word] = [1, 0]
    for word in d_5:
        if word in f_f:
            f_f[word][1] += 1
        else:
            f_f[word] = [0, 1]
    #print(f)
    _sum_ = 0
    for j in f_f:
        _sum_ = _sum_ + (f_f[j][0]*f_f[j][1])
    numerator = _sum_
    s_a = 0
    for j in f_f:
        s_a = s_a+ (f_f[j][0]**2)
    n_a = 0
    for j in f_f:
        n_a = n_a + (f_f[j][1]**2)
    denominator = math.sqrt(s_a)*math.sqrt(n_a)
    return  numerator/denominator
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
