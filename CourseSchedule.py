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
## leetcode problem: 207. Course Schedule
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 
# Constraints:
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 
def CourseSchedule(numCourses, prerequisites):
    # build the adjacency list for prereq
    prereq = [[] for i in range(numCourses)]
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    visiting = set()            # set of nodes on current dfs path
    def dfs(c):        
        if c in visiting:       # if c forms a cycle 
            return False
        if prereq[c] == []:     # if c can be taken
            return True  

        visiting.add(c)         
        for p in prereq[c]:     # if c's prereqs are good to go
            if not dfs(p):
                return False
        visiting.remove(c)      # c is good to go
        prereq[c] =  []    
        
        return True



    for i in range(numCourses): # check for every node in case there are multiple connected components
        if not dfs(i):
            return False

    return True        

     

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 2; prerequisites = [[1,0]]
print(CourseSchedule(numCourses, prerequisites))

# # --------------------------MAIN to TEST-------------------------------------
numCourses = 2; prerequisites = [[1,0],[0,1]]
print(CourseSchedule(numCourses, prerequisites))

