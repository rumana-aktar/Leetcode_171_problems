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
## leetcode problem: 117. Populating Next Right Pointers in Each Node II
# Medium

# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 
# Follow-up:
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.next = None
        self.val = key



def populatingNextRightPointerII(root):
    if not root:
        return root

    parent = root
    while parent:
        
        dummy = Node(0)
        tmp = dummy
        
        while parent:
            if parent.left:
                tmp.next = parent.left
                tmp = parent.left
            if parent.right:
                tmp.next = parent.right
                tmp = tmp.next

            if parent:    
                parent = parent.next
        
        parent = dummy.next

    return root


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(4);
root.left.right = Node(5)

root.right.right = Node(7)
populatingNextRightPointerII(root)


# # # --------------------------MAIN to TEST-------------------------------------
# root = Node(3)
# root.left = Node(5); root.right = Node(1)
# root.left.left = Node(6); root.left.right = Node(2)
# root.right.left = Node(0); root.right.right = Node(8)
# root.left.right.left = Node(7); root.left.right.right = Node(4)
# print(rightViewOfBinaryTree(root))

# # # --------------------------MAIN to TEST-------------------------------------
# root = Node(1)
# print(rightViewOfBinaryTree(root))




