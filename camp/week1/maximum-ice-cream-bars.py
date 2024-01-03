class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        val=coins
        while i<len(costs):
            val-=costs[i]
            if val == 0:
                return i+1
            elif val<0 and costs[0]<coins:
                return i
            elif val>0 and i==len(costs)-1:
                return len(costs) 
            i+=1
        return 0               





        