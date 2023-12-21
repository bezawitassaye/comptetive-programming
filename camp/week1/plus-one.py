class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        elem=int("".join(str(d) for d in digits)) + 1
        return list(map(int, str(elem)))