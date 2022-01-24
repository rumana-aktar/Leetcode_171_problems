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



## leetcode problem: 637. Average of Levels in Binary Tree
# Easy

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
 
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def averageOfLevelsOfBinaryTree(root):
    res = []
    q = deque()
    q.append(root)

    while q:
        q_len, sum_val = len(q), 0.0
        for _ in range(q_len):
            node = q.popleft()
            sum_val= sum_val + node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)    

    
        res.append(sum_val/q_len)    

    return res


# # --------------------------MAIN to TEST-------------------------------------
#root = [3,9,20,null,null,15,7]
root = Node(3)
root.left = Node(9) ; root.right = Node(20)
root.right.left = Node(15); root.right.right = Node(7)
print(averageOfLevelsOfBinaryTree(root))  

# # --------------------------MAIN to TEST-------------------------------------
root = [3,9,20,15,7]
root = Node(3)
root.left = Node(9) ; root.right = Node(20)
root.left.left = Node(15); root.left.right = Node(7)

# # --------------------------MAIN to TEST-------------------------------------
