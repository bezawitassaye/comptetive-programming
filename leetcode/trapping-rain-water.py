class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[0,height[0]]
        maxright=[0,height[-1]]
        res=0
        for i in range(2,len(height)):
            if height[i-1] > maxleft[-1]:
                maxleft.append(height[i-1])
            else:
                maxleft.append(maxleft[-1])


        for j in range(len(height)-3,-1,-1):
            if height[j+1] > maxright[-1]:
                maxright.append(height[j+1])
            else:
                maxright.append(maxright[-1])
        maxright.reverse()

  
        for k in range(len(height)):
            if min(maxright[k],maxleft[k]) - height[k] >=0:
                res+= min(maxright[k],maxleft[k]) - height[k]
        return res        
                       





        