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



## leetcode problem: 876. Middle of the Linked List
# Easy

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLL(head):
    cur = head
    print("\nThe list is: ", end = "")
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print("\n")

def middleOfLinkedList(head):
    slw, fst = head, head

    while fst and fst.next:
        slw = slw.next
        fst = fst.next.next

    printLL(slw)
    return slw    




# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
middleOfLinkedList(root)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
middleOfLinkedList(root)

# # --------------------------MAIN to TEST-------------------------------------
root = None
middleOfLinkedList(root)


# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(6)
middleOfLinkedList(root)
