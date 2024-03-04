# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        self.res=0
        def helper(cur,minn,maxx):
            if not cur:
                return
            self.res =max(self.res,abs(cur.val-minn),abs(maxx-cur.val))
            minn=min(minn,cur.val)
            maxx=max(maxx,cur.val)
            helper(cur.left,minn,maxx)
            helper(cur.right,minn,maxx)
        helper(root,root.val,root.val)
        return self.res       
        