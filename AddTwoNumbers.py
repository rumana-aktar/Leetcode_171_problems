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



## leetcode problem: 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

def printLL(head):
    cur = head
    print("\nThe list is: ", end = "")
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print("\n")

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        val = val1 + val2 + carry
        carry, val = val // 10, val % 10
        
        cur.next = ListNode(val)
        l1 = l1.next if l1 else None
        l2 = l2.next if l1 else None

    return dummy.next    



# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
