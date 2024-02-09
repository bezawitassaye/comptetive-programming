class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix) 
        c = len(matrix[0])
        self.new = [[0] * (c+1) for _ in range(r+1)]
        for row in range(r):
            pref = 0
            for col in range(c):
                pref += matrix[row][col]
                above = self.new[row][col + 1]
               
                self.new[row + 1][col + 1] = pref + above
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: 
        row1,row2,col1,col2=row1+1,row2+1,col1+1,col2+1
        return    self.new[row2][col2]-self.new[row1-1][col2]-self.new[row2][col1-1] +self.new[row1-1][col1-1]  
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)