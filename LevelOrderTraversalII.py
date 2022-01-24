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
## leetcode problem: 107. Binary Tree Level Order Traversal II
# Medium

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
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



def levelOrderTraversal(root):
    if not root:
        return []
    output = []
    q = deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level_out = []
        for _ in range(qLen):
            node = q.popleft()
            level_out.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(level_out)

    return output[::-1]


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(5);
root.right.right = Node(4)
print(levelOrderTraversal(root))


# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(8)
root.left.right.left = Node(7); root.left.right.right = Node(4)
print(levelOrderTraversal(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
print(levelOrderTraversal(root))



# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
print(levelOrderTraversal(None))


# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(80)

#root.left.left.left = None; root.left.left.left = None
root.left.right.left = Node(7); root.left.right.right = Node(4)

root.left.right.left.right = Node(70); 
print(levelOrderTraversal(root))
