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
    for key, value in sout:
        end = ''
        for _ in range(value):
            end += '#'
        print(key+' '+'-'+' '+end)

def main():
    '''
    main function
    '''

    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
