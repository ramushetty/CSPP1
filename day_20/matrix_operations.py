def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    new1 = []
    #new2 = []
    mat_len1 = len(m1)
    mat_len2 = len(m2[0])
    mat_len3 = len(m2)
    for index in range(mat_len1):
        new2 = []
        for y in range(mat_len2):
            sum1 = 0
            for x in range(mat_len3):
                sum1 += m1[index][x]*m2[x][y]
            new2.append(sum1)
        new1.append(new2)
    return new1
    '''
    add1=[]
    for i in range(len(m1)):
        add2=[]
        for (a,b) in zip(m1[i], m2[i]):
            add2.append(a*b)
        add1.append(add2)
    print(add1)
    '''
def add_matrix(m1, m2,):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''

    add1 = []
    for i in range(len(m1)):
        add2 = []
        for (a, b) in zip(m1[i], m2[i]):
            add2.append(a+b)
        add1.append(add2)
    return add1

def read_matrix(m1, m2, arr, arr1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    #count = 0
    first = 0
    fi = 0
    arr_len = len(arr)
    for index in range(arr_len):
        if arr[index] == len(m1):
            for i in range(arr[0]):
                if len(m1[i]) == arr[1]:
                    first = 1
    arr_len = len(arr1)
    for index in range(arr_len):
        if arr[index] == len(m2):
            for i in range(arr[0]):
                if len(m2[i]) == arr[1]:
                    fi = 2
    #print(count)
    if fi == 2 and first == 1:
        return True
    else:
        return False
def main():
    '''
    takes input
    '''
    # read matrix 1
    arr = list(map(int, input().split(',')))
    #print(arr)
    matrix1 = []
    matrix2 = []
    for i in range(arr[0]):
        for j in range(arr[1]):
            matrix1.append(list(map(int, input().split())))
            #print(matrix1)
            if len(matrix1) == arr[1]:
                break
            break
    #print(matrix1)
    # read matrix 2
    arr1 = list(map(int, input().split(',')))
    #print(arr1)
    for i in range(arr1[0]):
        for j in range(arr1[1]):
            matrix2.append(list(map(int, input().split())))
            if len(matrix2) == arr1[1]:
                break
            break
    #print(matrix2)
    #c_c = arr1[0]*arr1[1]
    if read_matrix(matrix1, matrix2, arr, arr1) == True:
    # add matrix 1 and matrix 2
        if arr[0] == arr1[0] and arr[1] == arr1[1]:
            print(add_matrix(matrix1, matrix2))
        else:
            print("Error: Matrix shapes invalid for addition")
            print("None")
        # multiply matrix 1 and matrix 2

        if arr[1] == arr1[0]:
            print(mult_matrix(matrix1, matrix2))
        else:
            print("Error: Matrix shapes invalid for mult")
            print("None")
    else:
        print("Error: Invalid input for the matrix")
if __name__ == '__main__':
    main()
