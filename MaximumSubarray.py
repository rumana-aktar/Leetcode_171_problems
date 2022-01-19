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



## leetcode problem: 53. Maximum Subarray
# Easy

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def maximumSubarray(nums):
    max_sum, cur_sum = 0, 0
    r = 0

    while r < len(nums):
        cur_sum += nums[r]
        max_sum = max( max_sum, cur_sum)
        r += 1

        if cur_sum < 0:
            cur_sum = 0

    return max_sum

# # --------------------------MAIN to TEST-------------------------------------
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(nums))
# # --------------------------MAIN to TEST-------------------------------------
nums = [1]
print(maximumSubarray(nums))
# # --------------------------MAIN to TEST-------------------------------------
nums = [5,4,-1,7,8]
print(maximumSubarray(nums))
