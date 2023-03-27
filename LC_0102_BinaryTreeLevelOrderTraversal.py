# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        answer = []
        
        if root is None:
            return answer
            
        cur = [root]
        next = []

        while len(cur) > 0:
            layer = []
            for node in cur:
                layer.append(node.val)
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)

            answer.append(layer)
            cur = next
            next = []
        
        return answer