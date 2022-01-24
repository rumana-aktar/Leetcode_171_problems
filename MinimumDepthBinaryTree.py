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
## leetcode problem: 111. Minimum Depth of Binary Tree
# Easy

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
 
# Constraints:
# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000


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
def minimumDepthOfBinaryTree(root):
    if not root:
        return 0
        
    q = deque()
    q.append(root)
    depth = 0

    while q:
        depth += 1
        q_len = len(q)
        for _ in range(q_len):
            node = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)    
            if node.right:
                q.append(node.right)

    return depth            


    
# # --------------------------MAIN to TEST-------------------------------------
# Input: root = [2,null,3,null,4,null,5,null,6]
root = None
print(minimumDepthOfBinaryTree(root))
     

# # --------------------------MAIN to TEST-------------------------------------
# Input: root = [3,9,20,null,null,15,7]
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(minimumDepthOfBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
# Input: root = [2,null,3,null,4,null,5,null,6]
root = Node(1)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.right = Node(5)
root.right.right.right.right = Node(6)
print(minimumDepthOfBinaryTree(root))

