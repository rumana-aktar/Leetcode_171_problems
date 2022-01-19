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



## leetcode problem: 41. First Missing Positive
# Hard

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1

# Constraints:
# 1 <= nums.length <= 5 * 105
# -231 <= nums[i] <= 231 - 1

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def firstMissingPositive(nums):
    n = len(nums)

    # replace any number <=0 with n+2
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 2

    # max missing positive number could be n
    # so for any positive number, make the value of corresponding index -negative
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            nums[val - 1] = - abs(nums[val -1])

    # the index of fiirst positive number indicates the missing number
    for i in range(n):
        if nums[i] > 0:
            return i + 1    

    return n+1


# # --------------------------MAIN to TEST-------------------------------------
nums = [1]
print(firstMissingPositive(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,2,3,4]
print(firstMissingPositive(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [3,4,-1,1]
print(firstMissingPositive(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [7,8,9,11,12]
print(firstMissingPositive(nums))
