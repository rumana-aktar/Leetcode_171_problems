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



## leetcode problem: 11. Container With Most Water
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def containerWithMostWater(height):
    l, r, mWater = 0, len(height)-1, -2**32

    while l < r:
        cWater = (r-l) * min(height[l], height[r])
        mWater = max(mWater, cWater)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return mWater


# # --------------------------MAIN to TEST-------------------------------------
height = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(height))

# # --------------------------MAIN to TEST-------------------------------------
height = [1,1]
print(containerWithMostWater(height))

# # --------------------------MAIN to TEST-------------------------------------
