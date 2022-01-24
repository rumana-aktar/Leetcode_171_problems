# # ---------------------------------------------------------------------------
#   Solution Author: Rumana Aktar 
#   Date: 12/28/2021
# 
#   For more information, contact:
#       Rumana Aktar
#       226 Naka Hall (EBW)
#       University of Missouri-Columbia
#       Columbia, MO 65211
#       rayy7@mail.missouri.edu
# # ---------------------------------------------------------------------------

# # ---------------------------------------------------------------------------
## leetcode problem: 417. Pacific Atlantic Water Flow
# Medium

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
 
# Constraints:
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def pacificAtlanticWaterFlow(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(),  set()
    res = []

    def dfs(r, c, ocean, prevHeight):
        
        if ((r,c) in ocean or                               # if [r,c] is already in ocean set
            r < 0 or r >= ROWS or c < 0 or c >= COLS or     # if [r,c] is out of bound
            heights[r][c] < prevHeight):                    # if its neighbour has low height; then water cannot flow
            return

        # now water can flow
        ocean.add((r,c))
        dfs(r + 1, c, ocean, heights[r][c])
        dfs(r - 1, c, ocean, heights[r][c])
        dfs(r, c + 1, ocean, heights[r][c])
        dfs(r, c - 1, ocean, heights[r][c])



    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])                     #top row touches pacific   
        dfs(ROWS -1, c, atl, heights[ROWS -1][c])         #bottom row touches atlantic   

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])                     #left column touches pacific 
        dfs(r, COLS -1, atl, heights[r][COLS -1])         #right column touches atlantic  

    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])

    return res            


# # --------------------------MAIN to TEST-------------------------------------
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlanticWaterFlow(heights))

# # --------------------------MAIN to TEST-------------------------------------
heights = [[2,1],[1,2]]
print(pacificAtlanticWaterFlow(heights))
