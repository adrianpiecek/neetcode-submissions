class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            y = i//3
            for j, val in enumerate(row):
                if val == '.':
                    continue
                x = j//3
                boxNo = 3*y + x
                if val in row_set[i] or val in col_set[j] or val in box_set[boxNo]:
                    return False
                else:
                    row_set[i].add(val)
                    col_set[j].add(val)
                    box_set[boxNo].add(val)
        
        return True
                