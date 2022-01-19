# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %  Solution Author: Rumana Aktar 
# %  Date: 01/05/2022
# %
# %  For more information, contact:
# %      Rumana Aktar
# %      226 Naka Hall (EBW)
# %      University of Missouri-Columbia
# %      Columbia, MO 65211
# %      rayy7@mail.missouri.edu
# # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



## leetcode problem: 74. Search a 2D Matrix
# Medium

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def search2DMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1

    while i>=0 and i<m and j>=0 and j<n:
        if matrix[i][j] == target:      return True
        elif matrix[i][j] < target:     i += 1
        else:                           j -= 1

    return False      

def search2DMatrixBinarySearch(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1

    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if matrix[mid//n][mid%n] == target:
            return True
        elif matrix[mid//n][mid%n] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return False                


# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3
print(search2DMatrixBinarySearch(matrix, target))

# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 13
print(search2DMatrixBinarySearch(matrix, target))

# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 60
print(search2DMatrixBinarySearch(matrix, target))

# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 23
print(search2DMatrixBinarySearch(matrix, target))

