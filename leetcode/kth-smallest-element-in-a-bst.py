# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        res=[]
        cur=root
        n=0
        
        while cur or res:
            while cur:
                res.append(cur)
                cur=cur.left
            cur=res.pop()    
            n+=1
            if k==n:
                return cur.val
            cur=cur.right        




