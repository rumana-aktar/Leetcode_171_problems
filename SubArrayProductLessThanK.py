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



## leetcode problem: 713. Subarray Product Less Than K
# Medium

# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Example 1:
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Example 2:
# Input: nums = [1,2,3], k = 0
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def subarrayProductLessThanK(nums, k):
    l, cnt, prod = 0, 0, 1

    for r in range(len(nums)):
        prod *= nums[r]

        if prod >= k:
            while prod >=k and l <= r:
                prod /= nums[l]
                l += 1

        if l <= r:
            cnt += r - l +1  
    return cnt              

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,1,1]; k = 1
print(subarrayProductLessThanK(nums, k))


# # --------------------------MAIN to TEST-------------------------------------
nums = [10,5,2,6]; k = 100
print(subarrayProductLessThanK(nums, k))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,2,3]; k = 0
print(subarrayProductLessThanK(nums, k))

# # --------------------------MAIN to TEST-------------------------------------
