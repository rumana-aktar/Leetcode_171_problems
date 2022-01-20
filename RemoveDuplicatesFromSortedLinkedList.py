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



## leetcode problem: 83. Remove Duplicates from Sorted List
# Easy

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

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

def removeDuplicatesSortedLinkedList(head):
    if head and not head.next:
        #printLL(head)
        return head
    
    cur, prev = head.next, head
    while cur:
        if cur.val == prev.val:
            prev.next, cur = cur.next, cur.next
        else:
            prev, cur = cur, cur.next

    #printLL(head)
    return head            

# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(3)
root.next.next = ListNode(3)
root.next.next.next = ListNode(-4)
root.next.next.next.next = ListNode(-4)
root.next.next.next.next.next = ListNode(2)
root.next.next.next.next.next.next = ListNode(2)
#removeDuplicatesSortedLinkedList(root)
# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
#removeDuplicatesSortedLinkedList(root)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(2)
root.next.next.next = ListNode(-4)
removeDuplicatesSortedLinkedList(root)
