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



## leetcode problem: 287. Find the Duplicate Number
# Medium

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
 
# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.


# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def findDuplicate(nums):
    duplicate = -1
    for i in range(len(nums)):
        val = abs(nums[i])
        if nums[val] < 0:
            duplicate = val
        else:
            nums[val] = - nums[val]

    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = - nums[i]        

    return duplicate            



# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3,4,2,2]
print(findDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [3,1,3,4,2]
print(findDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
