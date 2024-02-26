class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
      
        stack=[]
        res=0
        for i in range(len(arr)):
            while stack and arr[i]<stack[-1][1]:
                j,m=stack.pop()
                res+=(j-stack[-1][0] if stack else j+1)*m*(i-j)
                res %= (10 ** 9 +7)
            stack.append([i,arr[i]])
        for i in range(len(stack)):
            j,m = stack[i]
            res+=(j-stack[i-1][0] if i > 0 else j+1)*m*(len(arr)-j)
            res %= (10 ** 9 +7)
        return res           
        