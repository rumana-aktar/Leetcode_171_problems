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



## leetcode problem: 234. Palindrome Linked List
# Easy

# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
 
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 
# Follow up: Could you do it in O(n) time and O(1) space?

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def printLL(head):
    cur = head
    print("...The list is: ", end = "")
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print("\n")



def reverseLinkedList(head):
    prev = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = prev
        prev, cur = cur, tmp
    return prev

def isPalindrom(head):

    if head and not head.next:
        return True
    
    slw, fst, prev = head, head, None

    # find the middle
    while fst and fst.next:
        prev, slw, fst= slw, slw.next, fst.next.next
    prev.next = None    

    #reverse the 2nd half
    prev = None
    while slw:
        tmp = slw.next
        slw.next = prev
        prev, slw = slw, tmp
            
    # check palindrom; left will be shorter if there is odd number of nodes
    left, right = head, prev
    while left:
        if left.val != right.val:
            return False
        left, right = left.next, right.next   
    
    return True    





# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(0)
root.next.next.next.next = ListNode(2)
root.next.next.next.next.next = ListNode(3)
#head = reverseLinkedList(root)
print(isPalindrom(root))
#printLL(root)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
# root.next = ListNode(2)
# root.next.next = ListNode(1)
print(isPalindrom(root))

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(2)
print(isPalindrom(root))
#printLL(root)
