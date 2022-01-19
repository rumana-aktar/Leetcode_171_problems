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



## leetcode problem: 442. Find All Duplicates in an Array
# Medium

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1,2]
# Output: [1]

# Example 3:
# Input: nums = [1]
# Output: []
 
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def findAllDuplicate(nums):
    duplicates = []
    for i in range(len(nums)):
        val = abs(nums[i])
        if nums[val-1] < 0:
            duplicates.append(val)
        else:
            nums[val-1] = - nums[val-1]

    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = - nums[i]        

    return duplicates            



# # --------------------------MAIN to TEST-------------------------------------
nums = [4,3,2,7,8,2,3,1]
print(findAllDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,1,2]
print(findAllDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1]
print(findAllDuplicate(nums))
