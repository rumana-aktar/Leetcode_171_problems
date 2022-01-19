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



## leetcode problem: 658. Find K Closest Elements
# Medium

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

# Constraints:
# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

# # --------------------------Solution-------------------------------------
import os, bisect; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def kClosestInteger(nums, k, x):
    idx = bisect.bisect_left(nums, x)

    # if x is out of range
    if idx == len(nums):
        return nums[len(nums)-k: ]

    l, r = idx - k , idx
    if l < 0:
        l, r = 0, k 

    while r < len(nums) and abs(nums[l]-x) > abs(nums[r]-x):
        #print([nums[l], x, nums[r]])
        l += 1
        r += 1

    return nums[l:r]    





# --------------------------MAIN to TEST-------------------------------------
# arr = [1,2,3,4,5]; k = 4; x = 7
# print(kClosestInteger(arr, k,x))

# # # --------------------------MAIN to TEST-------------------------------------
# arr = [1,2,3,4,5]; k = 4; x = -1
# print(kClosestInteger(arr, k,x))

# # # --------------------------MAIN to TEST-------------------------------------
# arr = [0, 1, 2, 5, 10, 15, 21, 100, 115, 116]; k = 4; x = 20
# print(kClosestInteger(arr, k,x))

arr = [-2,-1,1,2,3,4,5]; k = 7; x = -3
print(kClosestInteger(arr, k,x))
