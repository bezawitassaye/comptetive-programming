class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        for i in range(len(candies)):
             ss=candies[i]+ extraCandies
             if ss >= maxx:
                 candies[i] =True
             else:
                  candies[i]=False
        return  candies          


           