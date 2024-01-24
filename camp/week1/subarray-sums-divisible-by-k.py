from collections import Counter
from itertools import accumulate

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return sum(r * (r-1) // 2 for _, r in Counter(map(lambda x: x % k, accumulate([0] + nums))).items())