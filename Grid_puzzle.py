#sudoku=[[0,4,1,2,5],[5,0,0,4,0],[0,5,0,3,1],[4,3,0,0,2],[1,0,3,0,0]]
#sudoku=[[1,0,3,4,5],[4,5,0,0,3],[0,3,0,0,1],[5,0,2,3,0],[3,4,0,1,2]]
digits=[1, 2, 3, 4, 5]
print('"Instructions"\n1.Enter the digits in row\n2.Entered digits should be space-separated\n3.Enter 0 in the space where digit needs to be added\n')
sudoku=[]
#To Enter the input
n=5
while n>=1:
    try:
        sudoku_row=list(map(int,input('Enter the row digits').split(' ')))
        if len(sudoku_row)!=5:
            raise
        sudoku.append(sudoku_row)
        n-=1
    except ValueError as Ve:
        print('Entered digit in not an integer\t Error:{0}'.format(Ve))
    except:
        print('Total number of digits is not of length 5,need to enter elements of length 5')

for row in sudoku:
    digit_to_add=[]
    #add digit_to_add with digit needs to be replaced with 0
    for i in digits:
        if i not in row:
            digit_to_add.append(i)
    index_value=row.index(0)
    #check if only one zero digit in row it will be replaced with number to be added
    if len(digit_to_add)==1:
        row.pop(index_value)
        row.insert(index_value, digit_to_add[0])
        digit_to_add.clear()
    else:
    #backtrace to check if the digit is not present in that row and column
        F=0
        for y in digit_to_add:
            if digits==sorted(row):
                break
            #column wise check through index values
            for z in sudoku:
                if z[index_value]==y:
                    digit_to_add.append(y)
                    break
                else:
                    F+=1
                    continue
            else:
                if F>=4:
                    row.pop(index_value)
                    row.insert(index_value, y)
                    try:
                        index_value=row.index(0, index_value + 1)
                    except ValueError:
                        index_value=0
                    F=0
    #printing the elements in row
    for elements in row:
        print(elements,end=' ')
    print()





