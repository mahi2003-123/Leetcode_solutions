class Solution(object):
    def isValidSudoku(self, board):
        row=[]
        for i in range(9):
            row.append(set())
        col=[]
        for j in range(9):
            col.append(set())
        boxes=[]
        for z in range(9):
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num=board[r][c]
                box=(r//3)*3+(c//3)
                if num in row[r]:
                    return False
                if num in col[c]:
                    return False
                if num in boxes[box]:
                    return False
                row[r].add(num)
                col[c].add(num)
                boxes[box].add(num)
        return True