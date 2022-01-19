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



## leetcode problem: 378. Kth Smallest Element in a Sorted Matrix
# Medium

# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
 
# Follow up:
# Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
import bisect

def kthSmallestInSortedMatrix(matrix, k):
    lo, hi, M = matrix[0][0], matrix[-1][-1], len(matrix)

    # return count of elements which are less than mid
    def less_k(m):
        cnt = 0
        for r in range(M):
            x = bisect.bisect_right(matrix[r], m)
            if x < 1:   break
            else:       cnt += x
        
        return cnt

    while lo < hi:
        mid = lo + (hi - lo) //2
        if less_k(mid) < k:
            lo = mid + 1
        else:
            hi = mid

    return lo            



# --------------------------MAIN to TEST-------------------------------------
matrix = [[1,5,9],[10,11,13],[12,13,15]]; k = 8
print(kthSmallestInSortedMatrix(matrix, k))


# # --------------------------MAIN to TEST-------------------------------------
matrix = [[-5]]; k = 1
print(kthSmallestInSortedMatrix(matrix, k))

# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,2], [1,3]]; k = 2
print(kthSmallestInSortedMatrix(matrix, k))


matrix = [[10, 20, 30, 40], 
          [15, 25, 35, 45], 
          [27, 29, 37, 48], 
          [32, 33, 39, 50]]; k =6
print(kthSmallestInSortedMatrix(matrix, k))

