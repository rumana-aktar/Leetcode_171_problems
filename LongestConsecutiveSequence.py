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



## leetcode problem: 128. Longest Consecutive Sequence
# Medium

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def longestConsecutiveSequence(nums):
    s = set(nums)
    max_len = 0

    for i in range(len(nums)):

        # start of a sequence
        if nums[i]-1 not in s:
            cur_length = 0
            while nums[i] + cur_length in s:
                cur_length += 1

            max_len = max (max_len, cur_length)
        

    return max_len            







# # --------------------------MAIN to TEST-------------------------------------
nums = [100,4,200,1,3,2]
print(longestConsecutiveSequence(nums))

# # --------------------------MAIN to TEST-------------------------------------
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutiveSequence(nums))

# # --------------------------MAIN to TEST-------------------------------------
