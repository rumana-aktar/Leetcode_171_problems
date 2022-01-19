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

def setMatrixZeros(matrix):
    m=len(matrix); n=len(matrix[0])
    row_set=set(); col_set=set()
        
        #get the rows and cols
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row_set.add(i)
                col_set.add(j)
        
    for r in row_set:
        for c in range(n):
            matrix[r][c]=0
    for c in col_set:
        for r in range(m):
            matrix[r][c]=0
                    
        
    return matrix


# # --------------------------MAIN to TEST-------------------------------------
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setMatrixZeros(matrix))


# # --------------------------MAIN to TEST-------------------------------------
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setMatrixZeros(matrix))

# # --------------------------MAIN to TEST-------------------------------------
