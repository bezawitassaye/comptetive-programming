from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digit = board[i][j]
                    if digit in rows[i] or digit in columns[j] or digit in boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    rows[i].add(digit)
                    columns[j].add(digit)
                    boxes[(i // 3) * 3 + (j // 3)].add(digit)

        return True