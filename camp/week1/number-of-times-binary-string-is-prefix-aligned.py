class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        first = [0] * len(flips)
        countt = 0
        max_index = 0
        
        for i in range(len(flips)):
            index = flips[i] - 1
            first[index] = 1
            max_index = max(max_index, index)
            
            if max_index == i:
                countt += 1
        
        return countt