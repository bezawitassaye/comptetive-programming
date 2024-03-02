# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
       mm=defaultdict(int)

       def helper(node):
           nonlocal mm
           if not node:
               return
          
           mm[node.val] = 1 + mm.get(node.val,0)
           helper(node.left)
           helper(node.right)
           
       helper(root)
       nn = max(mm.values(),default=0)
       result = [key for key ,value in mm.items() if value == nn]
       return result
      