class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for i in range(len(points)):
            res.append([points[i][0]**2+points[i][1]**2,[points[i][0],points[i][1]]])
        res.sort(key=lambda x:x[0])
        arr=[]
        for j in range(k):
            arr.append(res[j][1])
        return arr     

        