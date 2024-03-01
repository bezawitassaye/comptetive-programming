# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        def helper(node1,node2):
            if not node1 and not node2:
                return None
            new= TreeNode((node1.val if node1 else 0 ) + (node2.val if node2 else 0)) 
            new.right=helper(node1.right if node1 else None,node2.right if node2 else None)
            new.left=helper(node1.left if node1 else None,node2.left if node2 else None)
            return new
        return helper(root1,root2)        

