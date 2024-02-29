# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.hepler(root.left,root.right)
    def hepler(self,lr,rr):
        if lr == None and rr == None:
            return True
        if lr == None or rr == None:
            return False
        if lr.val != rr.val:
            return False        
        return self.hepler(lr.left,rr.right) and self.hepler(lr.right,rr.left)        


        