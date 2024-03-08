class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(string):
            if len(s)< 2:
                return ""
            cover = set(string)
            for i in range(len(string)):
                if not (string[i].lower() in cover and string[i].upper() in cover):
                    string1 = dfs(string[:i])
                    string2 = dfs(string[i + 1:])
                    return string2 if len(string2) > len(string1) else string1
            return string

        return dfs(s)       
        


        