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



## leetcode problem: 153. Find Minimum in Rotated Sorted Array
# Medium

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def minimumInSortedRotatedArray(nums):
    if len(nums) == 0:
        return -1
        
    if nums[0] < nums[len(nums)-1]:
        return nums[0]
        
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
            
        if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
            return nums[mid + 1]
        elif nums[0] <= nums[mid]:
            lo = mid + 1
        else:
            hi = mid -1
      
        return nums[0]


# # --------------------------MAIN to TEST-------------------------------------
nums = [3,4,5,1,2]
print(minimumInSortedRotatedArray(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [4,5,6,7,0,1,2]
print(minimumInSortedRotatedArray(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [11,13,15,17]
print(minimumInSortedRotatedArray(nums))
