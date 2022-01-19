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



## leetcode problem: 852. Peak Index in a Mountain Array
# Easy

# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1
 
# Constraints:
# 3 <= arr.length <= 104
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.

# Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def peakMountain(nums):
    lo, hi = 0, len(nums)-1

    if hi > 0 and nums[lo] > nums[lo + 1]:
        return lo

    if hi > 0 and nums[hi] > nums[hi-1]:
        return hi    

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if mid > 0 and nums[mid-1] < nums[mid] and mid < len(nums)-1 and nums[mid] > nums[mid + 1]:
            return mid
        elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
            lo = mid + 1
        elif mid > 0 and nums[mid-1] > nums[mid]:
            hi = mid - 1

    return -1            




# # --------------------------MAIN to TEST-------------------------------------
arr = [0,1,0]
print(peakMountain(arr))

# # --------------------------MAIN to TEST-------------------------------------
arr = [0,2,11,110, 300]
print(peakMountain(arr))

# # --------------------------MAIN to TEST-------------------------------------
arr = [0,10,51,2]
print(peakMountain(arr))
