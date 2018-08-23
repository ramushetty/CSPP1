'''
matrix addition and substraction
'''
def mult_matrix(m_1, m_2):
    '''
    matrix multiplication
    '''
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    new1 = []
    #new2 = []
    mat_len1 = len(m_1)
    mat_len2 = len(m_2[0])
    mat_len3 = len(m_2)
    for index in range(mat_len1):
        new2 = []
        for y_y in range(mat_len2):
            sum1 = 0
            for x_x in range(mat_len3):
                sum1 += m_1[index][x_x]*m_2[x_x][y_y]
            new2.append(sum1)
        new1.append(new2)
    return new1
def add_matrix(m_1, m_2,):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''

    add1 = []
    len_l = len(m_1)
    for i in range(len_l):
        add2 = []
        for (a_a, b_b) in zip(m_1[i], m_2[i]):
            add2.append(a_a+b_b)
        add1.append(add2)
    return add1

def read_matrix(m_1, m_2, arr, arr1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    #count = 0
    first = 0
    f_i = 0
    arr_len = len(arr)
    for index in range(arr_len):
        if arr[index] == len(m_1):
            for i in range(arr[0]):
                if len(m_1[i]) == arr[1]:
                    first = 1
    arr_len = len(arr1)
    for index in range(arr_len):
        if arr[index] == len(m_2):
            for i in range(arr[0]):
                if len(m_2[i]) == arr[1]:
                    f_i = 2
    #print(count)
    if f_i == 2 and first == 1:
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
    for _ in range(arr[0]):
        for _ in range(arr[1]):
            matrix1.append(list(map(int, input().split())))
            #print(matrix1)
            if len(matrix1) == arr[1]:
                break
            break
    #print(matrix1)
    # read matrix 2
    arr1 = list(map(int, input().split(',')))
    #print(arr1)
    for _ in range(arr1[0]):
        for _ in range(arr1[1]):
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
