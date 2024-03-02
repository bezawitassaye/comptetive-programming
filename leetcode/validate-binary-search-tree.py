# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,ll=float("-inf"),up=float("inf")):
            if not node:
                return True
          
            if not(ll < node.val < up) :
                return False
            if not helper(node.left,ll,node.val):
                return False
            if not helper(node.right,node.val,up):
                return False  
            return True      
        return helper(root)             
        