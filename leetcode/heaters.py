class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = []
        for house in houses:
            res.append(self.bsearch(house, heaters))
        return max(res)
    
    def bsearch(self, target, heaters):
        ch = float("inf")
        l = 0
        r = len(heaters) - 1
        
        if target in heaters:
            return 0
        
        while l <= r:
            mid = (l + r) // 2
            if heaters[mid] < target:
                ch = min(ch, target - heaters[mid])
                l = mid + 1
            else:
                ch = min(ch, heaters[mid] - target)
                r = mid - 1
        
        return ch
