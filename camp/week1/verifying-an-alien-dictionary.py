class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {c: i for i, c in enumerate(order)}
        
        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]
            
            if not self.is_lexicographically_sorted(prev_word, curr_word, char_map):
                return False
        
        return True
    
    def is_lexicographically_sorted(self, word1: str, word2: str, char_map: dict) -> bool:
        n1, n2 = len(word1), len(word2)
        min_len = min(n1, n2)
        
        for i in range(min_len):
            if word1[i] != word2[i]:
                if char_map[word1[i]] > char_map[word2[i]]:
                    return False
                else:
                    return True
        
        return n1 <= n2