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



## leetcode problem: 143. Reorder List
# Medium

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# # --------------------------Solution-------------------------------------
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

def reorderLinkedList(head):

    if not head or not head.next:
        return head

    # get the middle of the linkedList
    prev, slw, fst = None, head, head
    while fst and fst.next:
        prev, slw, fst = slw, slw.next, fst.next.next
    if prev:    prev.next = None
    left, right = head, slw

    # reverse the 'right' list    
    prev, cur = None, right
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    right = prev

    
    # generate a new linkedList by alternating left and right
    dummy = ListNode()
    cur = dummy
    while left and right:
        cur.next, left = left, left.next
        cur.next.next, right = right, right.next
        cur = cur.next.next

        
    if right:
        cur.next = right

    return dummy.next        
        

    # reverse the 2nd half of the linkedList

# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
printLL(reorderLinkedList(root))

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
printLL(reorderLinkedList(root))

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next.next = ListNode(5)
printLL(reorderLinkedList(root))
