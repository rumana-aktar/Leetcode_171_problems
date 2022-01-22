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



## leetcode problem: 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
 
# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def trappingRainWater(height):
    left_max = [-1 for i in range(len(height))]
    right_max = [-1 for i in range(len(height))]

    for i in range(1,len(height)):
        left_max[i] = max(left_max[i-1], height[i-1])

    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i+1])

    rainWater = 0
    for i in range(len(height)):
        curWater = max (0, min(left_max[i], right_max[i])-height[i])
        rainWater += curWater

    return rainWater        




# # --------------------------MAIN to TEST-------------------------------------
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingRainWater(height))

# # --------------------------MAIN to TEST-------------------------------------
height = [4,2,0,3,2,5]
print(trappingRainWater(height))

# # --------------------------MAIN to TEST-------------------------------------
