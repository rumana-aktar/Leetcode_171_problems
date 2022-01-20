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



## leetcode problem:  203. Remove Linked List Elements
# Easy

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []
 
# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

# # --------------------------Solution-------------------------------------
from PalindromeLinkedList import reverseLinkedList
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class ListNode:
    def __init__(self, x=0, next = None):
        self.val = x
        self.next = next

def printLL(head):
    cur = head
    print("\nThe list is: ", end = "")
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print("\n")

def removeListNode(head, val):
    # add dummy for edge case
    dummy = ListNode(val-1, head)
    
    # keep removing if val is found
    cur, prev = dummy, None
    while cur:
        if cur.val == val:
            prev.next, cur = cur.next, cur.next
        else:
            prev, cur = cur, cur.next

    #printLL(dummy.next)
    # return new head
    return dummy.next    



# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(0)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(1)
root.next.next.next.next = ListNode(0)
root.next.next.next.next.next = ListNode(0)
root.next.next.next.next.next.next = ListNode(0)
removeListNode(root, 0)


# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
removeListNode(root, 1)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
removeListNode(root, 2)
