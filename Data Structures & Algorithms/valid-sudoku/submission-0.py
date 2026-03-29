class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_l = [[i for i in board[k] if i!="."] for k in range(9)]
        col_l = [[board[i][s] for i in range(9) if board[i][s] !="."] for s in range(9)]
        box_l = [[board[i][j] for i in range(0+k,3+k) for j in range(0+l,3+l) if board[i][j]!="."] for k in range(0,9,3) for l in range(0,9,3)]
        full_l = row_l + col_l + box_l
        for i in range(len(full_l)):
            for j in range(len(full_l[i])):
                if full_l[i][j] in full_l[i][j+1:]:
                    print (full_l[i][j], full_l[i][j+1:])
                    return False
        return True