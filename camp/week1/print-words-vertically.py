class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        result = [''] * max_len
        
        
        for i in range(max_len):
            for word in words:
                if i < len(word):
                    result[i] += word[i]
                else:
                    result[i] += ' '
        
        return [word.rstrip() for word in result]