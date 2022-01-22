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



## leetcode problem: 977. Squares of a Sorted Array
# Easy

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()




# # --------------------------MAIN to TEST-------------------------------------
def sortedSquares(nums):
    res = [0 for i in range(len(nums))]
    l, r, k = 0, len(nums)-1, len(nums)-1

    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            res[k], l = nums[l]**2, l+1
        else:
            res[k], r = nums[r]**2, r-1
        k -= 1

    return res         


# # --------------------------MAIN to TEST-------------------------------------
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [-7,-3]
print(sortedSquares(nums))
