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



## leetcode problem: 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def containsDuplicate(nums):
    s = set()
        
    for x in nums:
        if x in s:
            return True
        else:
            s.add(x)
        
    return False

        


# # --------------------------MAIN to TEST-------------------------------------
nums = [1,2,3,1]
print(containsDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,2,3]
print(containsDuplicate(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
