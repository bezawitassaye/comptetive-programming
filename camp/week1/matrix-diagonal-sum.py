class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count=0
        column=len(mat[0])
        j=0
        while j<column:
            count+=mat[j][j]
            j+=1
        j=0
        while column:
            count+=mat[j][column-1]
            j+=1
            column-=1
        if len(mat[0]) %2 != 0:
            print(len(mat[0]))
            index=len(mat[0])//2
            count-=mat[index][index]
        return count        


        