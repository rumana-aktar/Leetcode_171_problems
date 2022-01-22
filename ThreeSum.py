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



## leetcode problem: 15. 3Sum
# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []
 
# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def threeSum(nums):

    nums.sort()
    res = []

    for i, val in enumerate(nums):

        if i > 0 and nums[i-1] == val:
            continue
        
        l, r = i+1, len(nums)-1
        
        while l < r : 
            
            if val + nums[l] + nums[r] < 0:
                l += 1
            elif val + nums[l] + nums[r] > 0:
                r -= 1
            else:
                res.append([val, nums[l], nums[r]])
                l += 1
                while l < r and nums[l-1] == nums[l]:
                    l += 1

    return res             





# # --------------------------MAIN to TEST-------------------------------------
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = []
print(threeSum(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [0]
print(threeSum(nums))

# %%
