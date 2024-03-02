class Solution:
    def bestClosingTime(self, customers: str) -> int:
    
        pre=[0]*(len(customers)+1)
        for i in range(len(customers)):
            if customers[i] == "N":
                pre[i+1]=pre[i]+1
            else:
                pre[i+1]=pre[i]
        post=[0]*(len(customers)+1)  
   

        for j in range(len(customers)-1,-1,-1):
            post[j]=post[j+1]
            if customers[j] == "Y":
                post[j]  += 1 

        minn,indx=float("inf"),0

        for i in range(len(post)):
            summ = post[i] + pre[i]
            if summ < minn:
                minn=summ
                indx=i
        return indx       

          

    
        