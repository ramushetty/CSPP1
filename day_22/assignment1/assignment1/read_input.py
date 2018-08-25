'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''
    main 
    '''
    inputt = int(input())
    stringg = []
    e_m = ''
    for i in range(inputt):
        stringg.append(list(map(str, input().split('\n'))))

    for i in range(inputt):
        #print(stringg)
        e_m = ''.join(stringg[i])
        print(e_m)


if __name__ == '__main__':
    main()
