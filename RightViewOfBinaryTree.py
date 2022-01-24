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
## leetcode problem: 199. Binary Tree Right Side View
# Medium

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



def rightViewOfBinaryTree(root):
    output = []
    q = deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        rightNode = None
        for _ in range(qLen):
            node = q.popleft()
            rightNode = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        output.append(rightNode)        

    return output


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(5);
root.right.right = Node(4)
print(rightViewOfBinaryTree(root))


# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(8)
root.left.right.left = Node(7); root.left.right.right = Node(4)
print(rightViewOfBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
print(rightViewOfBinaryTree(root))




# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(80)

#root.left.left.left = None; root.left.left.left = None
root.left.right.left = Node(7); root.left.right.right = Node(4)

root.left.right.left.right = Node(70); 
print(rightViewOfBinaryTree(root))
