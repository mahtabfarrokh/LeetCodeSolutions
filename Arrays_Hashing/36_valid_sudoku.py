class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    print("hi")
                    continue 
                    
                #check row
                for k in range(j+1, 9):
                    if board[i][j] == board[i][k]:
                        return False
                
                #check col
                for k in range(i+1, 9):
                    if board[i][j] == board[k][j]:
                        return False
                    
                #check square      
                for x in range(3):
                    for y in range(3):  
                        if (i == int(i/3)*3+x) and (j == int(j/3)*3+y): 
                            continue
                        if board[i][j] == board[int(i/3)*3+x][int(j/3)*3+y]:
                            return False
                        
        return True
