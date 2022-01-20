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



## leetcode problem: 
# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class ListNode:
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next

def printLL(head):
    cur = head
    print("\nThe list is: ", end = "")
    while cur:
        print(cur.val, end = " ")
        cur = cur.next
    print("\n")


def mergeSortedList(left, right):
    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.val <= right.val:
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next

        tail = tail.next 

    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next               




def sortLinkedList(head):

    if not head or not head.next:
        return head


    #get the middle and make left and right list
    prev, slw, fst = None, head, head
    while fst and fst.next:
        prev, slw, fst = slw, slw.next, fst.next.next

    if prev:
        prev.next = None    
    
    # devide and conquer
    left, right = head, slw
    left = sortLinkedList(left)
    right = sortLinkedList(right)
    
    # merge the two sorted sublist
    return mergeSortedList(left, right)

    

    





# #--------------------------MAIN to TEST-------------------------------------
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
printLL(sortLinkedList(root))

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(1)
printLL(sortLinkedList(root))

# # --------------------------MAIN to TEST-------------------------------------
root = ListNode(-30)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
printLL(sortLinkedList(root))
