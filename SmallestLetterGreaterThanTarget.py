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



## leetcode problem: 744. Find Smallest Letter Greater Than Target
# Easy

# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

# Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

# Example 3:
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"

# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def findSmallestLetterGreatetThanTarget(letters, target):
    lo, hi = 0, len(letters) - 1

    if target >= letters[hi] or target < letters[lo]:
        return letters[lo]

    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2

        if target >= letters[mid]:
            lo = mid 
        else:
            hi = mid 

    return letters[hi]            

        
        



            





# # # --------------------------MAIN to TEST-------------------------------------
# letters = ["c","f","j"]; target = "a"
# print(findSmallestLetterGreatetThanTarget(letters, target))

# # --------------------------MAIN to TEST-------------------------------------
letters = ["c","f","j"]; target = "c"
print(findSmallestLetterGreatetThanTarget(letters, target))

# # --------------------------MAIN to TEST-------------------------------------
letters = ["c","f","j"]; target = "d"
print(findSmallestLetterGreatetThanTarget(letters, target))
