class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[points[i][0] for i in range(len(points))]
        x.sort()
        widest=0
        for i in range(len(x)):
            if i+1 < len(x):
                n=abs(x[i] - x[i+1])
                widest=max(widest,n)
        return widest        