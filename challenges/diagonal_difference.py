'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x

Language
Python 3
More
123456789101112131415161718192021222324
    fptr.write(str(result) + '\n')

    fptr.close()

Line: 34 Col: 1

Test against custom input
'''

def diagonalDifference(arr):
    # [[1, 2, 3], [2, 5, 4], [7, 5, 6]]
    # 1 2 3
    # 2 5 4
    # 7 5 6
    # PD = 1+5+6 = 12 
    # SD = 3+5+7 = 15
    # RESULT : A BS(12 - 15) = 3
     
    primary_diagonal = 0
    secondary_diagonal = 0
    
    for index_pd, list_values in enumerate(arr, start=0):
        primary_diagonal += list_values[index_pd]
        index_sd = index_pd + 1
        secondary_diagonal += list_values[-index_sd]
             
    return abs(primary_diagonal - secondary_diagonal)


if __name__ == '__main__':
    print('\n\n\n ENTER THE LENGTH OF YOUR SQUARE MATRIX  \n\n')
    
    n = int(input("ENTER A VALUE HERE :::>  ").strip())
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input("ENTER E SEQUENCE OF VALUES :::>>  ").rstrip().split())))

    print(arr)
    result = diagonalDifference(arr)

    print(f'THE RESULT IS >>>>>>  {result}')