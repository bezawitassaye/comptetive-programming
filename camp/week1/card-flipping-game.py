from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        notinclude=set()
        for back,front in zip(backs,fronts):
            if back==front:
                notinclude.add(back)

        res=inf
        for i in backs+fronts:
            if i not in notinclude:
                res=min(res,i)
        return res if res!= inf else 0                
