class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        result=[1]
        pref=self.getRow(rowIndex - 1)
        for i in range(len(pref)-1):
            result.append(pref[i]+pref[i+1])
        result.append(1)   
        return result 

        

        