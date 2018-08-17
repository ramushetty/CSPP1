'''
    Document Distance - A detailed description is given in the PDF
'''
def numerator(fun_dic):
    '''
    returns numerator
    '''
    _sum_ = 0
    for keys in fun_dic:
        _sum_ = _sum_ + (fun_dic[keys][0]*fun_dic[keys][1])
    return _sum_
def denominator(fun_dic):
    '''
    returns denominator
    '''
    import math
    sum_1 = 0
    for keys in fun_dic:
        sum_1 = sum_1+ (fun_dic[keys][0]**2)
    sum_2 = 0
    for keys in fun_dic:
        sum_2 = sum_2 + (fun_dic[keys][1]**2)
    return math.sqrt(sum_1)*math.sqrt(sum_2)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import re
    dict_1 = ""
    dict_2 = ""
    dict_4 = []
    dict_5 = []
    fun_dic = {}
    dict_1 = dict1
    dict_2 = dict2
    new_dict1 = re.sub(r'[^a-zA-Z ]', '', dict_1).lower().strip().split()
    new_dict2 = re.sub(r'[^a-zA-Z ]', '', dict_2).lower().strip().split()
    stop_words = load_stopwords("stopwords.txt")
    #print(ne_1)
    #print(ne1)
    #print(loa)
    for word in new_dict1:
        if word not in stop_words:
            dict_4.append(word)
    for word in new_dict2:
        if word not in stop_words:
            dict_5.append(word)
    for word in dict_4:
        if word  in fun_dic:
            fun_dic[word][0] += 1
        else:
            fun_dic[word] = [1, 0]
    for word in dict_5:
        if word in fun_dic:
            fun_dic[word][1] += 1
        else:
            fun_dic[word] = [0, 1]
    #print(fun_dic)
    return  numerator(fun_dic)/denominator(fun_dic)
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    f_i = filename
    stopwords = {}
    with open(f_i, 'r') as f_i:
        for line in f_i:
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
