
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = collections.Counter()

        for i,j in matches:
            losses[i] += 0
            losses[j] +=1
        ans = [[],[]]
        for x in losses.keys():
            if losses[x] <= 1:
                ans[losses[x]].append(x)
        ans[0].sort()
        ans[1].sort()
        return ans            

 