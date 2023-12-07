class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ss=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if j == i :
                    continue
                else:
                    if boxes[j]=="1":
                        ss[i]+=abs(i-j)
        return ss                    
        