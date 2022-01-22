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

def threeSum(nums, target):

    nums.sort()
    closest_sum = sum(nums[0:3])

    for i, val in enumerate(nums):
        l, r = i+1, len(nums)-1        
        while l < r : 
            cur_sum = val + nums[l] + nums[r]
            
            if abs(cur_sum-target) < abs(closest_sum-target):
                if cur_sum == target:
                    return cur_sum
                closest_sum = cur_sum
            elif cur_sum < target:
                l  += 1
            else:
                r -= 1                    

    return closest_sum             





# # --------------------------MAIN to TEST-------------------------------------
nums = [-1,2,1,-4]; target = 1
print(threeSum(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = [0,0,0]; target = 1
print(threeSum(nums, target))



# %%
