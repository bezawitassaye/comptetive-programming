class Solution:
    def totalMoney(self, n: int) -> int:
        m = n // 7
        rem = n % 7
        ans = (m / 2) * (56 + 7 *(m - 1 ))

         
        for i in range(1 + m, rem + m + 1):
            ans += i
        
        return int(ans)



        