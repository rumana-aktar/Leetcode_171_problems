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



## leetcode problem:268. Missing Number
# Easy
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def missingNumberSummation(nums):
    n = len(nums)
    natural_sum = (n*(n+1))//2

    actual_sum = 0
    for x in nums:
        actual_sum += x

    return natural_sum - actual_sum    


def missingNumber(nums):

    found_zero = False
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = len(nums)+1
            found_zero = True
        
    
    for i in range(len(nums)):
        val = abs(nums[i])
        if val <= len(nums):
            nums[val-1] = - abs(nums[val-1])

    
    if found_zero == False:
        return 0

    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1    


# # --------------------------MAIN to TEST-------------------------------------
nums = [3,0,1]
print(missingNumberSummation(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumberSummation(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [0,1]
print(missingNumberSummation(nums))
