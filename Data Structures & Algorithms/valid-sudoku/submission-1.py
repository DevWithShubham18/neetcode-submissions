class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         
        for i in range(0, 9):
            a = []
            for j in range(0, 9):

                if board[i][j] == ".":
                    continue
                
                if board[i][j] in a:
                    return False
                a.append(board[i][j])
                

        
        for i in range(0, 9):
            b = []
            for j in range(0, 9):

                if board[j][i] == ".":
                    continue
                
                if board[j][i] in b:
                    return False
                b.append(board[j][i])
        

        for row in range(0, 9, 3):

            for col in range(0, 9, 3):

                c = []

                for i in range(row, row + 3):

                    for j in range(col, col + 3):

                        if board[i][j] == ".":

                            continue

                        if board[i][j] in c:

                            return False

                        c.append(board[i][j])

                
        return True