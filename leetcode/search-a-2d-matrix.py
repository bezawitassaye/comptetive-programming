class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top=0
        bot=row-1
        while top <= bot:
            Row=(top + bot)//2
            if target > matrix[Row][-1]:
                top = Row + 1
               
            elif target < matrix[Row][0]:
                bot = Row - 1
              
            else:
                break
        if  not( top <= bot):
            return False  
        Row = (top + bot)//2
        l,r=0,col-1

        while l<=r:
            mid = (l+r)//2
            if target > matrix[Row][mid]:
                l = mid + 1
            elif target < matrix[Row][mid]:
                r = mid -1
            else:
                return True
        return False                    

        