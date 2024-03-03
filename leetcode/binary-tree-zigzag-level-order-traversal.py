# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        
        q = deque([root] if root else [])

        while q:
            l=[]
            for i in range(len(q)):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            l=reversed(l) if len(res) % 2 else l
            res.append(l)
        return res        



