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
## leetcode problem: 100. Same Tree
# Easy

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 
def SameTree(p, q):
    if not p and not q:     #both null
        return True
    if not p or not q:      #one of them null
        return False
    if p.val != q.val:      #both non null but val is not equal
        return False    

    return SameTree(p.left, q.left) and SameTree(p.right, q.right)

# # --------------------------MAIN to TEST-------------------------------------
p = [1,2,3]; q = [1,2,3]
p = Node(1);
p.left = Node(2); p.right= Node(3)

q = Node(1);
q.left = Node(2); q.right= Node(3)

print(SameTree(p,q))

# # --------------------------MAIN to TEST-------------------------------------
p = [1,2]; q = [1,None,2]
p = Node(1);
p.left = Node(2); 

q = Node(1);
q.right= Node(2)
print(SameTree(p,q))


# # --------------------------MAIN to TEST-------------------------------------
p = [1,2,1]; q = [1,1,2]
p = Node(1);
p.left = Node(2); p.right= Node(1)

q = Node(1);
q.left = Node(1); q.right= Node(2)
print(SameTree(p,q))
