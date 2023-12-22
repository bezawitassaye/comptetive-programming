class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        
        container = []
        for i in range(row + col - 1):
            diagonal = []
            for j in range(max(0, i - col + 1), min(i + 1, row)):
                diagonal.append(mat[j][i - j])
            
            if i % 2 == 0:
                container.extend(diagonal[::-1])
            else:
                container.extend(diagonal)
        
        return container