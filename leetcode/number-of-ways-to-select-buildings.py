class Solution:
    def numberOfWays(self, s: str) -> int:
        count = 0
        pre0 = [0] * (len(s) + 1)
        post0 = [0] * (len(s) + 1)
        pre1 = [0] * (len(s) + 1)
        post1 = [0] * (len(s) + 1)

        for i in range(len(s)):
            if s[i] == "0":
                pre0[i+1] = pre0[i]+1
                pre1[i+1] = pre1[i]
            else:
                pre1[i+1] = pre1[i]+1
                pre0[i+1] = pre0[i]
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                post0[i] = post0[i+1] + 1
                post1[i] = post1[i+1]
            else:
                post1[i] = post1[i+1] + 1
                post0[i] = post0[i+1]
        # print(pre0)
        # print(post0)  
        # print(pre1)
        # print(post1)      
        for j in range(1,len(s)-1):
            if s[j] == "0":
                count +=  pre1[j+1] * post1[j+1]
            else:
                count +=  pre0[j+1] * post0[j+1]
        return count
                   




        


        