class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        column = len(strs[0])
        for i in range(column):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    count += 1
                    break
        return count