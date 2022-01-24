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
## leetcode problem: 116. Populating Next Right Pointers in Each Node
# Medium

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000
 
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



def populatingNextRightPointer(root):
    if not root:
        return root

    cur = root
    while cur.left:
        parent = cur
        while parent:
            parent.left.next = parent.right
            if parent.next:
                parent.right.next = parent.next.left
            parent = parent.next
        cur = cur.left  
    return root


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2); root.right = Node(3)
root.left.left = Node(5); root.left.right = Node(6);
root.right.left = Node(50); root.right.right = Node(60);
populatingNextRightPointer(root)

