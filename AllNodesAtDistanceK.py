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
## leetcode problem: 


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



def allNodesAtDistanceK(root, target, k):
    visited, parents, output = set(), {}, []
    q = deque()
    q.append(root)
    l = 0
    
    if root:
        parents[root] = None

    # BFS: store the parents of all nodes in parents
    while q:
        qLen = len(q)
        for _ in range(qLen):
            node = q.popleft()
            if node.left:
                parents[node.left] = node
                q.append(node.left)
            if node.right:
                parents[node.right] = node    
                q.append(node.right)

    # BFS: process like a graph    
    q.append(target)
    visited.add(target)
    while q:
        qLen = len(q)
        
        for _ in range(qLen):
            node = q.popleft()
            
            if l == k:
                output.append(node.val)
            
            if node.left:
                if node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                
                
            if node.right:
                if node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)

            if parents[node]:
                if parents[node] not in visited:
                    q.append(parents[node])
                    visited.add(parents[node])

        l += 1        

    

    return output

# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(8)
root.left.right.left = Node(7); root.left.right.right = Node(4)
print(allNodesAtDistanceK(root, root.left, 2))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
print(allNodesAtDistanceK(root, root, 3))




# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(5); root.right = Node(1)
root.left.left = Node(6); root.left.right = Node(2)
root.right.left = Node(0); root.right.right = Node(8)

#root.left.left.left = None; root.left.left.left = None
root.left.right.left = Node(7); root.left.right.right = Node(4)
print(allNodesAtDistanceK(root, root.left, 2))
