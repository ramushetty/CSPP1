'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
    frequency count 
    '''
    out = dictionary
    sout = sorted(out.items())
    for k,v in sout:
        end = ''
        for i in range(v):
            end += '#'
        print(k+' '+'-'+' '+end)

def main():
    '''
    main function
    '''

    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
