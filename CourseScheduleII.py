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
## leetcode problem: 210. Course Schedule II
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]
 
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 
def CourseScheduleII(numCourses, prerequisites):
    # build the adjacency list for prereq
    prereq = [[] for i in range(numCourses)]
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    visited, cycle = set(), set()          # set of nodes on current dfs path
    output = []
    def dfs(c):        
        if c in cycle:       # if c forms a cycle 
            return False
        if c in visited:     # if c can be taken
            return True  

        cycle.add(c)         
        for p in prereq[c]:     # if c's prereqs are good to go
            if not dfs(p):
                return False
        cycle.remove(c)      # c is good to go
        visited.add(c)
        output.append(c)
        
        return True



    for i in range(numCourses): # check for every node in case there are multiple connected components
        if not dfs(i):
            return []

    return output        

     

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 2; prerequisites = [[1,0]]
print(CourseScheduleII(numCourses, prerequisites))

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 2; prerequisites = [[1,0],[0,1]]
print(CourseScheduleII(numCourses, prerequisites))

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(CourseScheduleII(numCourses, prerequisites))

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 1; prerequisites = []
print(CourseScheduleII(numCourses, prerequisites))
