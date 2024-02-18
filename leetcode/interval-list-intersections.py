class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]

        for i in range(len(firstList)):
            for j in range(len(secondList)):
                if firstList[i][0]<secondList[j][1] and secondList[j][0] < firstList[i][1]:
                    res.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
                elif firstList[i][0] == secondList[j][1]:
                    res.append([firstList[i][0],secondList[j][1]])
                elif firstList[i][1] == secondList[j][0]:
                    res.append([firstList[i][1],secondList[j][0]])    
        
        
        return res            
        