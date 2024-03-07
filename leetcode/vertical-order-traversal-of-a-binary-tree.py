# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashset = defaultdict(lambda: defaultdict(list))
        
        def tra(root, row, col):
            if not root:
                return

            hashset[col][row] += [root.val]
            tra(root.left, row + 1, col - 1)
            tra(root.right, row + 1, col + 1)
        
        tra(root, 0, 0)
        
        res = []
        for col, cols in sorted(hashset.items()):
            res.append([])
            for row, rows in sorted(cols.items()):
                res[-1] += sorted(rows)
        
        return res
