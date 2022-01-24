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
## leetcode problem: 310. Minimum Height Trees
# Medium

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. You can return the answer in any order.
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Example 1:
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

# Example 2:
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Constraints:
# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 
def minimumHeightTrees(n, edges):
    if n <= 2:
        return [i for i in range(n)]

    # make the adjacency list
    adj = [[] for i in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # computer degree
    deg = [0 for i in range(n)]
    for i in range(len(adj)):
        deg[i] = len(adj[i])

    q = deque()
    for i, x in enumerate(deg):
        if x == 1:
            q.append(i)

    
    while q:
        output = []
        qLen = len(q)
        for _ in range(qLen):
            cur = q.popleft()
            output.append(cur)

            # for cur, decrease the degree of each of cur's neighbor by 1
            for nei in adj[cur]:
                deg[nei] -= 1
                if deg[nei] == 1:
                    q.append(nei)

    return output    


# # --------------------------MAIN to TEST-------------------------------------
n = 3; edges = [[0,1], [0,2]]
print(minimumHeightTrees(n, edges))

# # --------------------------MAIN to TEST-------------------------------------
n = 4; edges = [[1,0],[1,2],[1,3]]
print(minimumHeightTrees(n, edges))

# # --------------------------MAIN to TEST-------------------------------------
n = 6; edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(minimumHeightTrees(n, edges))
