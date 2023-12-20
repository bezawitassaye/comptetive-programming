class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
         rows = len(matrix)
         columns = len(matrix[0])
         transposed = [[0] * rows for _ in range(columns)]
         print(transposed)
         for i in range(rows):
             for j in range(columns):
                 transposed[j][i] = matrix[i][j]

         return transposed