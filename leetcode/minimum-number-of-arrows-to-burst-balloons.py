class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i :i[1])
        count=1
        end=points[0][1]
        i=1
        while i < len(points):
            if points[i][0] > end:
                count+=1
                end=points[i][1]
                i+=1
            else:
                i+=1      
        return count      
                     

