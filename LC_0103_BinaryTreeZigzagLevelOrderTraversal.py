# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        if root is None:
            return answer
        
        cur = deque()
        cur.append(root)
        next = deque()

        while len(cur) > 0:
            layer = []
            if len(answer) % 2 == 0:
                while len(cur) != 0:
                    node = cur.popleft()
                    layer.append(node.val)
                    if node.left is not None:
                        next.append(node.left)
                    if node.right is not None:
                        next.append(node.right)
            else:
                while len(cur) != 0:
                    node = cur.pop()
                    layer.append(node.val)
                    if node.right is not None:
                        next.appendleft(node.right)
                    if node.left is not None:
                        next.appendleft(node.left)
            
            answer.append(layer)
            cur = next
            next = deque()
        
        return answer


