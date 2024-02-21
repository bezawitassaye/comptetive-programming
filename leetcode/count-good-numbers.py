class Solution:
    def __init__(self):
         self.MOD = 1000000007

    def countGoodNumbers(self, n: int) -> int:
       
        even=n//2 + n%2
        odd = n//2
        return (self.power(5,even) * self.power(4,odd)) % self.MOD 
    def power(self,x,y):
        if y ==0:
            return 1
        ans=self.power(x,y//2)
        ans*=ans
        ans%=self.MOD
        if y % 2==0:
            return ans
        return ans*x % self.MOD         
        