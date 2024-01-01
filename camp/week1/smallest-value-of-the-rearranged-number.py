class Solution:
    def smallestNumber(self, num: int) -> int:
     
        if num > 0:
            num=list(str(num))
            for i in range(len(num)):
                for j in range(i+1,len(num)):
                    if int(num[j]) < int(num[i]):
                        num[i],num[j]=num[j],num[i] 
            if "0" in num:
                for k in num:
                    if k!= "0":
                        index=num.index(k)
                        num[0],num[index]=num[index],num[0]
                       
                        break
                return int("".join(num)) 
            else:
                return int("".join(num))                  
                        
            
        elif num<0:
            num*=-1
            num=list(str(num))
            num.sort()
            num=num[::-1]
            
            return int("".join(num))*-1 
        else:
            return 0    